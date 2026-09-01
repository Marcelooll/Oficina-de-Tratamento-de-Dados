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
Durante a oficina, nosso foco será o **Desafio 1**. Os demais são desafios extras (opcionais) para quem quiser se aprofundar!

1. **Desafio 1 (Obrigatório - Básico):** `desafio1/bcdata.sgs.22784.csv`. Tratamento de tipos de dados (converter string para número e formatar datas).
2. **Desafio 2 (Opcional - Intermediário):** `desafio2/CargosVagosVacancias_202607.ods`. Lidar com arquivos de planilhas e tratar dados faltantes (nulos).
3. **Desafio 3 (Opcional - Avançado):** `desafio3/Hash-*.p7s`. Lidar com extração de múltiplos arquivos não-estruturados/binários e consolidá-los.

**Regra de Ouro:** Para cada desafio, o resultado final deve ser salvo como um arquivo chamado `tratado.csv` dentro da pasta do respectivo desafio (ex: `desafio1/tratado.csv`).

## 🚀 Como Rodar e Validar
1. Clone o projeto: `git clone [link-do-seu-repositorio]`
2. Instale as dependências: `pip install pandas` (e possivelmente `odfpy` para o desafio 2)
3. Crie seus scripts Python para resolver cada desafio, salvando o output sempre como `tratado.csv` na respectiva pasta.
4. **Validação:** Não é preciso usar o terminal! 
   - Dê dois cliques no arquivo `validador.html` (ele abrirá no seu navegador).
   - Arraste o seu arquivo `tratado.csv` recém-criado para a tela e descubra na hora se você passou no desafio!