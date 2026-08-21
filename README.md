Oficina: Tratamento de Dados (Data Cleaning)

Bem-vindos! Este repositório é o guia da nossa oficina de tratamento de dados. O objetivo é demonstrar, na prática, como transformar uma base de dados "bruta" em um ativo valioso para análise.

---

Objetivo
Transformar uma base pública inconsistente em um dataset limpo, estruturado e reprodutível, utilizando Python e a biblioteca `pandas`. Queremos mostrar que, na Engenharia de Dados, o tratamento é tão importante quanto a análise em si.

Base de Dados
Para esta oficina, utilizaremos o dataset do **[BCB - Banco Central do Brasil - ex: Aluguel de equipamentos - mensal - despesa]**.
- **Por que esta base?** Ela é real, reflete problemas encontrados no mercado brasileiro (valores decimais como texto, erros de acentuação, dados faltantes) e nos permite realizar um "faxinão" que faz sentido para qualquer um.

Slides da Apresentação
Acompanhe nossa explicação através dos slides (disponíveis em [LINK_DOS_SLIDES]):
- **Parte 1:** Por que dados "sujos" existem? (O impacto no negócio).
- **Parte 2:** O fluxo de tratamento (Diagnóstico → Limpeza → Padronização → Validação).
- **Parte 3:** Demonstração ao vivo (O código em ação).

## 🧰 Kit de Sobrevivência (Comandos)
Nosso script utiliza os seguintes comandos `pandas`:
- `df.info()` e `df.isnull().sum()`: Diagnóstico inicial.
- `df.drop_duplicates()`: Remoção de redundância.
- `df.dropna()` / `df.fillna()`: Tratamento de buracos.
- `df['coluna'].str.strip()`: Limpeza de texto.
- `df['coluna'].astype(tipo)`: Conversão correta de dados.

## 💡 Atividade para os Participantes
Durante a oficina, desafiaremos os presentes a realizar o seguinte:
1. **O Desafio do "Detetive":** Analisar o arquivo `dados_brutos.csv` e listar 3 anomalias que eles encontram apenas olhando o arquivo.
2. **Implementação:** Seguir nosso script para corrigir essas 3 anomalias usando as funções que explicamos.
3. **Verificação:** Rodar um novo comando que valide se as anomalias foram corrigidas.

## 🚀 Como Rodar
1. Clone o projeto: `git clone [link-do-seu-repositorio]`
2. Instale: `pip install pandas`
3. Execute: `python tratamento.py`
4. Compare `dados_brutos.csv` com `dados_tratados.csv`.