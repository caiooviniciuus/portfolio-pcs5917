# Aula 3 — Resultados

Execução: 13/10/2026.

Usei **200 áudios do ASVspoof 5**, com 100 legítimos e 100 falsos, e executei a atividade localmente no lugar do Drive e do Colab. A amostra ocupa 43,16 MiB; os demais arquivos baixados ficaram preservados.

Com librosa, extraí 52 características por áudio, sem erros. Na análise do treino, os desvios dos MFCCs 17, 15 e 14 mostraram as maiores diferenças, com valores menores nos falsos e sobreposição entre as classes. A duração média também diferiu, mas não entrou no modelo.

Treinei uma regressão logística com 159 áudios e testei nos outros 41, sem repetir locutores entre os grupos. A padronização foi ajustada só no treino. O modelo acertou **36 de 41 áudios: 87,80% de acurácia, 88,37% de F1 para áudio falso e 0,9738 de ROC-AUC**. Foram 3 legítimos classificados como falsos e 2 falsos como legítimos.

O resultado se limita a esta amostra. A atividade foi realizada localmente, com adaptação das etapas de Drive e Colab.

## Arquivos

- [Notebook executado](../../notebooks/aula_03_deteccao_audio_falso.ipynb).
- [Características](features_publicas.csv), [amostras](manifesto_publico.csv) e [ranking exploratório](ranking_features_treino.csv).
- [Métricas](metricas_teste.json), [previsões](predicoes_teste.csv) e [configuração](configuracao.json).
- [Gráfico exploratório](../../images/aula-03/eda-features-treino.png) e [matriz de confusão/ROC](../../images/aula-03/avaliacao-teste.png).

Os áudios e arquivos com caminhos locais ficam em `dados/aula-03/`, fora do Git. As instruções de execução estão no notebook.
