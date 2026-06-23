# Lab 2 - CMC-13: Criacao de Classificadores baseado em Dados

## Sobre o Projeto

Trabalho em grupo da disciplina CMC-13 (Introducao a Ciencia de Dados) - Prof. Paulo Andre Castro.
O objetivo e criar classificadores de machine learning para prever rotatividade de clientes (customer churn).

**Prazo de entrega: 25/junho/2026**

## Estrutura do Projeto

```
Lab2/
├── material/                        # Enunciado e dados (NAO MODIFICAR)
│   ├── lab2_cmc13_2026.pdf          # Enunciado do laboratorio
│   ├── lab2_cmc13_dados_treinamento.csv  # Dados de treinamento (440k linhas)
│   └── lab2_cmc13_dados_teste.csv        # Dados de teste (64k linhas)
├── notebooks/                       # Codigo do projeto
│   ├── 1_preparacao_dados.ipynb     # Preparacao e analise exploratoria
│   ├── 2_A_tradicionais.ipynb       # Modelo KNN / Arvore de Decisao / SVM
│   ├── 2_B_redes_neurais.ipynb      # Modelo MLP (MultiLayer Perceptron)
│   ├── 2_C_comites.ipynb            # Modelo Random Forest / AdaBoost / XGBoost
│   └── 3_analise_comparativa.ipynb  # Comparacao de desempenho dos modelos
├── relatorio/                       # Relatorio final (LaTeX -> PDF)
│   ├── tex/
│   ├── imagens/
│   └── ignore/
└── CLAUDE.md                        # Este arquivo
```

## Dados

- **Variavel alvo:** `Churn` (0 = cancelou, 1 = nao cancelou)
- **Atributos:** CustomerID, Age, Gender, Tenure, Usage Frequency, Support Calls, Payment Delay, Subscription Type, Contract Length, Total Spend, Last Interaction
- Os dados de treinamento e teste estao separados em arquivos distintos. Usar `../material/` como caminho relativo nos notebooks.

## Tarefas do Projeto

1. **Preparacao dos Dados** (`1_preparacao_dados.ipynb`) - Limpeza, analise exploratoria, tratamento de dados faltantes/ruido
2. **Modelo Tradicional** (`2_A_tradicionais.ipynb`) - KNN, Arvore de Decisao ou SVM
3. **Redes Neurais** (`2_B_redes_neurais.ipynb`) - MLP (MultiLayer Perceptron)
4. **Comites** (`2_C_comites.ipynb`) - Random Forest, AdaBoost, XGBoost
5. **Analise Comparativa** (`3_analise_comparativa.ipynb`) - Metricas: acuracia, precision, recall, F1-score, Kappa
6. **Relatorio** (`relatorio/`) - PDF final com descricao dos procedimentos e resultados

## Regras para o Claude

- Sempre responder em portugues brasileiro.
- Usar scikit-learn como framework principal. Outros frameworks (TensorFlow, PyTorch) podem ser usados para redes neurais.
- Sempre adicionar celulas markdown descritivas antes de cada celula de codigo nos notebooks.
- Nunca modificar os arquivos dentro de `material/`. Eles sao somente leitura.
- Ao criar modelos, sempre avaliar com as metricas: acuracia, precision, recall, F1-score e Kappa statistic.
- Sempre treinar com `lab2_cmc13_dados_treinamento.csv` e testar com `lab2_cmc13_dados_teste.csv`.
- Nao inventar dados ou resultados. Sempre executar o codigo para obter os resultados reais.

## Boas Praticas de GitHub para o Grupo

### Branches

- **A branch `main` e protegida.** Ninguem deve commitar diretamente nela.
- Cada membro deve criar uma branch para trabalhar. Use o padrao:
  - `feat/<nome>/<descricao>` - para novas funcionalidades (ex: `feat/joao/modelo-knn`)
  - `fix/<nome>/<descricao>` - para correcoes (ex: `fix/maria/fix-preprocessing`)
- Quando terminar, abra um **Pull Request** para a `main` e peca revisao de pelo menos um colega.

### Commits

- Escreva mensagens de commit claras e em portugues. Exemplos:
  - "Adiciona modelo KNN com validacao cruzada"
  - "Corrige tratamento de valores faltantes na coluna Age"
  - "Atualiza analise comparativa com metricas Kappa"
- Faca commits pequenos e frequentes. Evite commits gigantes com muitas mudancas.

### Fluxo de Trabalho

1. Antes de comecar a trabalhar: `git pull origin main`
2. Crie sua branch: `git checkout -b feat/seu-nome/sua-tarefa`
3. Faca suas alteracoes e commits
4. Envie sua branch: `git push origin feat/seu-nome/sua-tarefa`
5. Abra um Pull Request no GitHub
6. Apos aprovacao e merge, delete a branch remota

### Conflitos

- Se houver conflitos no Pull Request, resolva localmente:
  1. `git checkout main && git pull origin main`
  2. `git checkout sua-branch && git merge main`
  3. Resolva os conflitos, faca commit e push novamente
- Comunique-se com o grupo antes de alterar arquivos que outros estao editando.

### O que NAO fazer

- Nao faca `git push --force` na `main`.
- Nao commite arquivos desnecessarios (dados grandes, checkpoints, `.ipynb_checkpoints/`).
- Nao altere trabalho de colegas sem avisar.
