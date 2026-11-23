# Aula 8 — Geração e detecção de trojans

O Grupo A (Arthur Moriggi Pimenta, Caio Vinícius Ribeiro da Silva e Roberto Spinelli Filho) trocou dois conjuntos de 20 amostras com o Grupo E. O Grupo A preparou as variantes do PicoRV32 e avaliou o AES recebido. O Grupo E classificou o PicoRV32.

## Relatório

- [Relatório final em PDF](relatorio-aula08.pdf), de 17/11/2026. A cópia é idêntica à versão publicada no [portfólio do Roberto](https://github.com/peninha/portfolio-pcs5917/blob/a18f97242c1b7ea21401b1ae238b229a70cf8a99/output/pdf/relatorio-aula08.pdf).

## PicoRV32 — conjunto preparado pelo Grupo A

O golden model foi o PicoRV32 em Verilog, na revisão `ef203c2b0a3fb793280f5114941416c425c5b461`, com recorte RV32I e interface nativa de memória. O relatório registra interação manual com o Codex (GPT-6 Astra) para produzir 10 variantes legítimas e 10 trojans. Os IDs internos B01–B10 e T01–T10 foram embaralhados em S01–S20. [Registro do processo](https://github.com/peninha/portfolio-pcs5917/blob/a18f97242c1b7ea21401b1ae238b229a70cf8a99/outros/aula-08-trojan/docs/PROCESSO.md)

[Comparação por amostra](comparacao_picorv32.csv) registra a classe esperada, a resposta do Grupo E e o acerto por ID.

O cruzamento do gabarito com a devolutiva confirma **5 verdadeiros positivos, 10 verdadeiros negativos, 0 falsos positivos e 5 falsos negativos**. A acurácia foi de **75% (15/20)**, o recall de **50% (5/10)** e o F1 de **66,7%**. Os falsos negativos foram S01, S06, S07, S08 e S13.

## AES — conjunto avaliado pelo Grupo A

O Grupo A usou o Codex para localizar diferenças entre os 20 códigos C++ recebidos (A01–A20) e interpretá-las à luz das regras do Grupo E. A01 serviu como ponto de comparação textual. [Registro do processo](https://github.com/peninha/portfolio-pcs5917/blob/a18f97242c1b7ea21401b1ae238b229a70cf8a99/outros/aula-08-trojan/docs/PROCESSO.md)

[Classificação por amostra](avaliacao_grupo_e.csv) preserva os 20 rótulos enviados, com dez registros em cada classe.

O relatório registra **20/20 acertos, 100% de recall, nenhum falso positivo e nenhum falso negativo**, conforme a confirmação do Grupo E. O repositório de origem registra essa confirmação como retorno comunicado em conversa. A mensagem original ou um gabarito independente do Grupo E seria necessário para verificar o 20/20 diretamente. [Resultados consolidados](https://github.com/peninha/portfolio-pcs5917/blob/a18f97242c1b7ea21401b1ae238b229a70cf8a99/outros/aula-08-trojan/docs/RESULTADOS.md)

## Evidência da troca e revisão conjunta

O arquivo original da atividade registra a entrega cega do PicoRV32, o formulário, o gabarito e os resultados devolvidos. As duas versões do Google Sheets pedidas no enunciado seguem sem link ou exportação identificados. [Índice da origem](https://github.com/peninha/portfolio-pcs5917/blob/a18f97242c1b7ea21401b1ae238b229a70cf8a99/outros/aula-08-trojan/docs/ARQUIVOS.md)

O relatório propõe uma revisão em formato *purple team* após a abertura do gabarito, com comparação das justificativas dos dois grupos. O lote adicional AES/Gemini ainda estava sem gabarito confirmado no registro consultado. [Resultados consolidados](https://github.com/peninha/portfolio-pcs5917/blob/a18f97242c1b7ea21401b1ae238b229a70cf8a99/outros/aula-08-trojan/docs/RESULTADOS.md)
