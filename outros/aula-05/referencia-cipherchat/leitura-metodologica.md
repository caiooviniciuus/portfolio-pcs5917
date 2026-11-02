# CipherChat — leitura e adaptação local

Referência: Yuan et al. (2024), *GPT-4 Is Too Smart To Be Safe: Stealthy Chat with LLMs via Cipher*, ICLR 2024. [Artigo oficial](https://proceedings.iclr.cc/paper_files/paper/2024/file/ed4c38fe7899d3653acf39b2102af8ba-Paper-Conference.pdf).

A seção 3 descreve a combinação de papel de especialista, explicação da cifra, demonstrações e conversão de entrada/saída. A seção 4 separa validade da comunicação e violação de segurança. A análise da Tabela 3 compara demonstrações nocivas e seguras; os resultados dependem também da capacidade do modelo de compreender a cifra. Isso orienta a separação entre falha de codificação e preservação da regra nesta atividade.

Usei exemplos seguros, três tarefas inteiramente fictícias e modelos locais. Implementei César +3, ASCII decimal e um controle textual com as mesmas demonstrações. Os pedidos em português foram normalizados sem acentos nas três condições. Esse recorte não reproduz o dataset, os modelos ou todas as variantes do artigo, nem permite aplicar suas taxas ao experimento local.

O código de referência usa funções de codificação/decodificação e consultas aos modelos. A adaptação usa a API do Ollama e arquivos JSON incrementais; os arquivos originais de referência não são executados.

## Pareceres do OpenReview

O fórum e as APIs públicas retornaram HTTP 403 nesta sessão. Os pareceres e as respostas dos autores não puderam ser lidos. Não foram inferidas avaliações, notas de revisão ou alterações solicitadas pelos revisores. [Fórum indicado no enunciado](https://openreview.net/forum?id=MbfAK4s61A).
