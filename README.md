# Oficina: Tratamento de Dados (Data Cleaning)

> **Bem-vindo à aula de Tratamento de Dados!**  
> Este projeto foi desenvolvido para ensinar a transformar dados brutos e desorganizados em tabelas limpas, confiáveis e prontas para análise utilizando Python e a biblioteca Pandas.

---

## Roteiro Pedagógico e Conceitos da Aula

### Slide 1: Pergunta Provocativa
* **Título:** Por que dados "sujos" geram decisões erradas?
* **Abertura:** *"Você já recebeu uma mensagem no WhatsApp que entendeu totalmente errado só por causa de uma vírgula?"*

---

### Slide 2: O Subsumor 1 — O Poder da Pontuação e da Sintaxe (Linguagem Humana x Código)
* **Exemplo do Dia a Dia (Ruído no Texto):**
  * Uma simples vírgula muda todo o sentido:
    * `"Vamos comer, gente!"` vs. `"Vamos comer gente!"`.
  * Excesso de espaços e caracteres soltos:
    * `"Oi,,,   tudo    bem???!!"` (para uma pessoa é legível, mas para um algoritmo é ruído).
* **O Análogo em Python:**
  Em Ciência de Dados, dados de formulários chegam com espaços excedentes e caracteres despadronizados:
  ```python
  nome_usuario = "   mArIaS2  "
  nome_limpo = nome_usuario.strip().lower()
  # Resultado: 'marias2'
  ```
  > **No Banco de Dados:** Sem essa limpeza, o sistema cadastrará `"Maria"`, `"maria "` e `"MARIA"` como três entidades distintas.

---

### Slide 3: O Subsumor 2 — A Foto no Escuro e o "Ruído" nos Dados
* **Exemplo do Dia a Dia (Tratamento de Imagem):**
  * Uma foto tirada no escuro apresenta ruído digital. Antes da publicação, ajusta-se a iluminação e aplicam-se filtros de redução de ruído.
* **O Análogo em Python:**
  * Imagens são matrizes numéricas (pixels). Tratar dados consiste em remover discrepâncias (*outliers*) e inconsistências para tornar a base analítica confiável.

---

### Slide 4: O Subsumor 3 — A Planilha de Despesas (Dados Ausentes e Inconsistentes)
* **Exemplo do Dia a Dia:**
  * Uma lista de despesas em grupo registrada de forma heterogênea:
    * Lucas: `R$ 50,00`
    * Beatriz: `cinquenta reais`
    * Matheus: *em branco*
    * Gabriel: `-R$ 50,00`
  * **Problema:** A soma automática falhará devido à mistura de tipos numéricos e de texto.
* **O Análogo em Python (Pandas):**
  ```python
  import pandas as pd

  # 1. Imputação de dados ausentes com zero:
  df['Valor'] = df['Valor'].fillna('0.00')

  # 2. Conversão de tipo de dados para float:
  df['Valor_Numerico'] = pd.to_numeric(df['Valor'], errors='coerce')
  ```

---

## Síntese dos Conceitos

| Situação | Dado Bruto | Instrução em Python | Resultado Esperado |
| :--- | :--- | :--- | :--- |
| **Erros de caixa e espaços** | `"  são paulo   "` e `"SAO PAULO"` | `.str.strip().str.lower()` | `"sao paulo"` (Registro padronizado) |
| **Separadores e nulos** | `"50,00"` e células em branco | `.fillna('0.00')` e `.str.replace(',', '.')` | Ponto flutuante somável (`float`) |
| **Registros duplicados** | Linhas idênticas na tabela | `df.drop_duplicates()` | Registro único por entidade |

---

## Os 3 Desafios da Oficina

Cada desafio possui seu arquivo de entrada bruto e deve ser resolvido escrevendo o script diretamente na plataforma web:

---

### Desafio 1: A Lista de E-mails do Evento (Nível 1)
* **Entrada:** `desafio1/emails_brutos.csv`
* **Especificação técnica:**
  ```python
  import pandas as pd

  # 1. Carregar a lista de e-mails
  df = pd.read_csv("desafio1/emails_brutos.csv")

  # 2. Imputar e-mails em branco
  df["email"] = df["email"].fillna("email_nao_informado@dominio.com")

  # 3. Remover espaços soltos nas extremidades
  df["email"] = df["email"].str.strip()

  # 4. Padronizar em letras minúsculas
  df["email"] = df["email"].str.lower()
  ```

---

### Desafio 2: Planilha de Despesas do Churrasco (Nível 2)
* **Entrada:** `desafio2/despesas_churrasco.csv`
* **Especificação técnica:**
  ```python
  import pandas as pd

  # 1. Carregar as despesas
  df = pd.read_csv("desafio2/despesas_churrasco.csv")

  # 2. Imputar valores não informados com zero
  df["valor"] = df["valor"].fillna("0.00")

  # 3. Substituir vírgulas por pontos decimais
  df["valor"] = df["valor"].astype(str).str.replace(",", ".")

  # 4. Converter tipo para float
  df["valor"] = df["valor"].astype(float)

  # Agregação:
  print(f"Total: R$ {df['valor'].sum():.2f}")
  ```

---

### Desafio 3: Lista de Presença da Oficina (Nível 3)
* **Entrada:** `desafio3/lista_presenca.csv`
* **Especificação técnica:**
  ```python
  import pandas as pd

  # 1. Carregar a lista de presença
  df = pd.read_csv("desafio3/lista_presenca.csv")

  # 2. Padronizar cidades em MAIÚSCULAS
  df["cidade"] = df["cidade"].str.strip().str.upper()

  # 3. Padronizar nomes no formato Título
  df["nome"] = df["nome"].str.strip().str.title()

  # 4. Eliminar registros duplicados
  df = df.drop_duplicates()
  ```

---

## Execução do Gabarito Oficial

Você pode executar a solução de referência através do script `gabarito.py`:

```bash
python gabarito.py
```

---

## Plataforma Web de Execução e Validação (`validador.html`)

A plataforma permite aos alunos escreverem e executarem o código Python diretamente na interface web:

1. Abra o arquivo **`validador.html`** no seu navegador.
2. Selecione o desafio a ser executado (**Desafio 1**, **Desafio 2** ou **Desafio 3**).
3. Escreva ou modifique o código no editor de código Python integrado.
4. Clique em **Executar e Validar Código**.
5. **Recursos da plataforma:**
   - **Execução WebAssembly (Pyodide):** Execução nativa do Python e Pandas no navegador.
   - **Console de Saída:** Exibição imediata das saídas de `sys.stdout` (`print`).
   - **Diagnóstico Tecnológico de Erros:** Explicitação de exceções (`KeyError`, `AttributeError`, `SyntaxError`) com orientações técnicas em português.
   - **Painel de Dados Brutos:** Visualização da tabela de entrada original antes do processamento.
   - **Guia de Código:** Modal de referência com a documentação dos métodos do Pandas.