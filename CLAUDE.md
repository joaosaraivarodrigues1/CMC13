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
│   ├── lab2_cmc13_dados_treinamento.csv  # Dados de tre
inamento (440k linhas)
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

### Filosofia de Trabalho: Investigar e Expor

O Claude deve agir como um **investigador**, nao como um tomador de decisoes. O grupo e quem decide.

**Princípios:**

1. **Mostrar, nao concluir.** Priorizar sempre graficos, tabelas e visualizacoes que exponham o comportamento dos dados. Nao ler os dados internamente e decidir o que e importante — expor visualmente para que o grupo analise.

2. **Nunca agir sem mostrar.** Antes de qualquer transformacao (remover outliers, dropar colunas, tratar nulos, fazer encoding, normalizar), DEVE primeiro:
   - Mostrar o estado atual dos dados com graficos/tabelas
   - Explicar em celula markdown o que foi observado e o que se propoe fazer
   - Somente aplicar a transformacao apos o grupo aprovar
   - Mostrar o resultado apos a transformacao (antes vs depois)

3. **Separar descoberta de acao.** Se algo for descoberto durante a analise (ex: coluna com muitos nulos, distribuicao enviesada, correlacao forte):
   - Adicionar uma celula markdown descrevendo a descoberta com evidencias visuais
   - Propor possiveis acoes, mas NAO executar automaticamente
   - Aguardar aprovacao do grupo

4. **Nada e obvio.** Mesmo decisoes aparentemente simples (ex: "CustomerID nao e relevante") devem ser justificadas visualmente. Mostrar o grafico ou tabela que sustenta a decisao.

5. **Graficos e tabelas primeiro, texto depois.** A ordem em cada etapa deve ser:
   - Codigo que gera a visualizacao/tabela
   - Markdown com a interpretacao e proposta (se houver)
   - Nunca o inverso (nunca concluir antes de mostrar)

### Imagens nos Notebooks

- Todas as figuras geradas nos notebooks DEVEM ser salvas na pasta `relatorio/imagens/`.
- Usar `plt.savefig('../relatorio/imagens/<nome>.png', dpi=150, bbox_inches='tight')` antes de `plt.show()`.
- Padrao de nomes: `<num_notebook>_<secao>_<descricao>.png`. Exemplos:
  - `1_prep_histogramas_numericas.png`
  - `1_prep_correlacao_pearson.png`
  - `1_prep_kde_treino_vs_teste.png`
  - `1_prep_distribuicao_por_churn.png`
  - `2a_trad_matriz_confusao_knn.png`
  - `2a_trad_curva_roc_knn.png`
  - `2b_rn_loss_por_epoca.png`
  - `2b_rn_matriz_confusao_mlp.png`
  - `2c_com_feature_importance_rf.png`
  - `2c_com_matriz_confusao_rf.png`
  - `3_comp_barplot_metricas.png`
  - `3_comp_curvas_roc_todos.png`
- Nunca usar espacos ou caracteres especiais nos nomes. Apenas letras minusculas, numeros e underscores.

### Relatorio LaTeX

- O relatorio esta em `relatorio/relatorio.tex`.
- Para compilar (de dentro da pasta `relatorio/`):
  ```
  pdflatex -output-directory=ignore relatorio.tex && cp ignore/relatorio.pdf relatorio.pdf
  ```
  No Windows:
  ```
  pdflatex -output-directory=ignore relatorio.tex && copy ignore\relatorio.pdf relatorio.pdf
  ```
- O PDF final fica em `relatorio/relatorio.pdf`.
- Todos os arquivos auxiliares (.aux, .log, .out, etc.) vao para `relatorio/ignore/`.
- As imagens sao referenciadas no LaTeX apenas pelo nome (ex: `\includegraphics{1_prep_correlacao_pearson.png}`), pois o `\graphicspath` ja aponta para `imagens/`.

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

