"""
Módulo compartilhado do Lab 2 — CMC-13.

Centraliza configuração do MLflow, função de avaliação e logging,
evitando duplicação de código entre os notebooks 2A, 2B, 2C e 3.
"""

import os
import subprocess
import socket
import time
import mlflow
from mlflow.tracking import MlflowClient
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, cohen_kappa_score, classification_report,
    confusion_matrix, ConfusionMatrixDisplay
)

# ── Configuração do MLflow ──────────────────────────────────────
_NOTEBOOKS_DIR = os.path.dirname(os.path.abspath(__file__))
_DB_PATH = os.path.join(_NOTEBOOKS_DIR, "mlflow.db").replace("\\", "/")
_BACKEND_URI = f"sqlite:///{_DB_PATH}"

TRACKING_URI = "http://127.0.0.1:5000"
EXPERIMENT_NAME = "Lab2-Churn"


def _servidor_ativo():
    """Verifica se o servidor MLflow está respondendo."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        try:
            s.connect(("127.0.0.1", 5000))
            return True
        except (ConnectionRefusedError, OSError):
            return False


def _iniciar_servidor():
    """Inicia o servidor MLflow em background se não estiver rodando."""
    if _servidor_ativo():
        return

    print("Iniciando servidor MLflow em background...")
    subprocess.Popen(
        [
            "mlflow", "server",
            "--backend-store-uri", _BACKEND_URI,
            "--host", "127.0.0.1",
            "--port", "5000",
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=subprocess.CREATE_NO_WINDOW
        if os.name == "nt" else 0,
    )

    # Aguardar o servidor subir (máx 15s)
    for _ in range(30):
        time.sleep(0.5)
        if _servidor_ativo():
            print("Servidor MLflow pronto em http://127.0.0.1:5000")
            return
    raise RuntimeError("Servidor MLflow não subiu em 15 segundos.")


# Garante que o servidor esteja rodando ao importar o módulo
_iniciar_servidor()

mlflow.set_tracking_uri(TRACKING_URI)
mlflow.set_experiment(EXPERIMENT_NAME)

_client = MlflowClient(tracking_uri=TRACKING_URI)


def avaliar_modelo(nome, y_true, y_pred):
    """Avalia um modelo, printa o relatório e retorna dict com métricas."""
    metricas = {
        'Modelo': nome,
        'Acuracia': accuracy_score(y_true, y_pred),
        'Precision': precision_score(y_true, y_pred),
        'Recall': recall_score(y_true, y_pred),
        'F1-Score': f1_score(y_true, y_pred),
        'Kappa': cohen_kappa_score(y_true, y_pred),
    }
    print(f'\n=== {nome} ===')
    print(classification_report(y_true, y_pred, target_names=['Não cancelou', 'Cancelou']))
    print(f'Kappa: {metricas["Kappa"]:.4f}')
    return metricas


def logar_mlflow(metricas, params, artefatos=None, tags=None):
    """Registra métricas, parâmetros, artefatos e tags no run MLflow ativo."""
    for k, v in params.items():
        mlflow.log_param(k, v)
    for k, v in metricas.items():
        if k != 'Modelo':
            mlflow.log_metric(k.lower().replace('-', '_'), v)
    if artefatos:
        for caminho in artefatos:
            mlflow.log_artifact(caminho)
    if tags:
        mlflow.set_tags(tags)


def iniciar_run(run_name, notebook, params, tags_extra=None):
    """Inicia um run MLflow com tags padronizadas.

    Cada execução cria um novo run — o histórico completo é preservado.
    Use buscar_melhores_runs() para obter apenas o melhor de cada modelo.

    Uso:
        with iniciar_run("MLP-v1", "2B", params):
            model.fit(...)
            logar_mlflow(metricas, params)
    """
    modelo = params.get('modelo', run_name)

    # Detectar versão do dataset automaticamente
    dados_dir = os.path.join(_NOTEBOOKS_DIR, "dados_processados")
    n_features = "?"
    features = "?"
    if os.path.exists(os.path.join(dados_dir, "X_train.parquet")):
        import pandas as pd
        cols = pd.read_parquet(os.path.join(dados_dir, "X_train.parquet"), columns=[]).columns.tolist()
        # Ler apenas os nomes das colunas (0 linhas)
        n_features = str(len(cols))
        features = ", ".join(cols)

    tags = {
        'notebook': notebook,
        'modelo': modelo,
        'n_features': n_features,
        'features': features,
    }
    if tags_extra:
        tags.update(tags_extra)
    return mlflow.start_run(run_name=run_name, tags=tags)


def buscar_melhores_runs():
    """Busca o melhor run (por F1-Score) de cada modelo no experimento.

    Returns:
        DataFrame com uma linha por modelo, ordenado por F1-Score desc.
    """
    import pandas as pd

    runs = mlflow.search_runs(
        filter_string="status = 'FINISHED'",
        order_by=["metrics.f1_score DESC"],
    )

    if runs.empty:
        print("Nenhum run finalizado encontrado.")
        return pd.DataFrame()

    colunas_map = {
        'tags.modelo': 'Modelo',
        'metrics.acuracia': 'Acuracia',
        'metrics.precision': 'Precision',
        'metrics.recall': 'Recall',
        'metrics.f1_score': 'F1-Score',
        'metrics.kappa': 'Kappa',
    }

    colunas_existentes = [c for c in colunas_map if c in runs.columns]
    df = runs[colunas_existentes].rename(columns=colunas_map)

    # Segurança extra: deduplicar pelo run mais recente de cada modelo
    df = df.drop_duplicates(subset='Modelo', keep='first')
    df = df.set_index('Modelo')

    return df
