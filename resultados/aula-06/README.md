# Aula 6 — Avaliação humana e automática

Resultados consolidados em 4 de novembro de 2026, no trabalho de Arthur Moriggi Pimenta, Caio Vinícius Ribeiro da Silva e Roberto Spinelli Filho.

## Arquivos

- [Planilha Ataques](Ataques.xlsx): aba `dados` com 203 registros e aba `HEPIC_Resultados_2026-11-04` com a exportação humana de 152 itens, suas fases, notas e decisões.
- [HEPIC em PDF](HEPIC.pdf): protocolo elaborado pelo grupo.
- [Notebook com saídas](llm_judge.ipynb): avaliações Qwen e JEV preparadas por Arthur.
- [CSV Qwen](resultados_llm_as_judge.csv) e [CSV JEV](resultados_jev_as_judge.csv): resultados originais de 177 registros, sem alteração.
- [Exportação HEPIC em CSV](hepic-resultados-2026-11-04.csv): conteúdo da aba humana da planilha.
- [Comparação por item](comparacao-humana-2026-11-04.csv): 151 itens, com IDs de origem, fase, nota humana, notas dos juízes e discordância.
- [Métricas da comparação](comparacao-humana-2026-11-04.json): contagens, matrizes de confusão, concordâncias e kappas.
- [Comparação entre juízes](comparacao-juizes.json): comparação automática nos 177 registros.
- [Relatório final](../../artigo/relatorio-aula06.pdf), [fonte LaTeX](../../artigo/relatorio-aula06.tex) e [referências](../../artigo/refs-aula06.bib).
- Figuras do relatório: [painel do HEPIC](../../artigo/images/hepic-painel.jpeg) e [adjudicação](../../artigo/images/hepic-adjudicacao.jpeg).
- [Pasta pública no Drive](https://drive.google.com/drive/folders/1MtFY4XPaf2Zg-MkHYEF9YyVR8DU0lz11).

## Conjuntos e resultados

A base consolidada tem 203 registros, incluindo 26 acrescentados após a execução dos juízes. Os CSVs automáticos abrangem os 177 anteriores. Não foram executados novamente durante esta análise.

O HEPIC usou 152 itens: dois exemplos de referência, um reservado marcado como inconclusivo, nove itens de calibração e 140 de avaliação. Foram 197 julgamentos individuais: 27 de calibração e 170 de avaliação. A distribuição inicial teve 112 itens com uma nota e 28 com duas; dois itens receberam uma terceira nota. Um deles exigiu adjudicação, com nota final 1.

A comparação usa os 151 itens com nota humana final: duas referências, nove de calibração e 140 de avaliação. O caso inconclusivo foi excluído das três avaliações. A vinculação foi conferida por modelo e resposta, distinguindo respostas repetidas pela condição ou rodada.

| Avaliação | Nota 0 | Nota 1 | Nota 2 | ASR | Concordância com humanos | Kappa não ponderado |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Humana | 138 | 2 | 11 | 7,28% | — | — |
| Qwen | 140 | 6 | 5 | 3,31% | 88,08% | 0,204 |
| JEV | 144 | 1 | 6 | 3,97% | 96,03% | 0,683 |

O Qwen não identificou nenhum dos 11 sucessos humanos; o JEV identificou seis. Nos 177 registros, as proporções brutas de nota 2 foram 4,52% para Qwen e 3,95% para JEV. Essas contagens incluem controles e rodadas de uma mesma trajetória.

## Limites e reprodução

- O conjunto humano foi selecionado por disponibilidade. Dos 140 itens, 112 têm apenas uma avaliação; 113 das 170 notas individuais não têm justificativa.
- O juiz automático recebe tarefa e resposta, sem o sistema de referência, o prompt completo, a identificação dos controles ou a decodificação do CipherChat.
- O Qwen foi carregado do Hugging Face em quatro bits NF4, com semente 42, até 300 novos tokens e sem amostragem. O JEV foi chamado pela API de decisões da OpenRouter. Os detalhes estão no notebook e no relatório.
- O notebook sobrescreve colunas no mesmo DataFrame. Preserve separadamente os resultados de cada juiz. Uma célula de diagnóstico usa `_id` antes de defini-lo; a revisão do modelo é impressa, mas não fixada no carregamento.
- A leitura do Qwen aceita JSON ou extrai a nota por expressão regular. O CSV não conserva a saída bruta nem identifica o uso dessa alternativa. Não há resultado de teste de repetibilidade.
- `subconjunto_ids.csv` é a seleção antiga de dez itens e não define os 140 usados na comparação final. `resumo-verificado.json` documenta a conferência inicial da execução Qwen, anterior à consolidação humana.
