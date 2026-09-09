# Oficina: Tratamento de Dados (Data Cleaning) 🧹📊

> **Bem-vindo à sua primeira aula de Tratamento de Dados!**  
> Este projeto foi desenvolvido para iniciantes absolutos. Aqui você vai aprender, de forma prática e mastigada, como transformar dados desorganizados do cotidiano em tabelas limpas, confiáveis e prontas para análise no Python.

---

## 💡 Roteiro Pedagógico e Conceitos da Aula

### Slide 1: Pergunta Provocativa
* **Título:** Por que dados "sujos" geram decisões erradas?
* **Abertura:** *"Você já recebeu uma mensagem no WhatsApp que entendeu totalmente errado só por causa de uma vírgula?"*

---

### Slide 2: O Subsumor 1 — O Poder da Pontuação e da Sintaxe (Linguagem Humana x Código)
* **Exemplo do Dia a Dia (Ruído no Texto):**
  * Uma simples vírgula muda todo o sentido:
    * `"Vamos comer, gente!"` vs. `"Vamos comer gente!"` (a falta da vírgula transforma uma refeição em canibalismo!).
  * Excesso de espaços e caracteres soltos:
    * `"Oi,,,   tudo    bem???!!"` (para uma pessoa é legível, mas para um robô ou IA é puro ruído).
* **O Análogo em Python:**
  Em Ciência de Dados, dados de formulários chegam cheios de espaços e letras misturadas:
  ```python
  nome_usuario = "   mArIaS2  "
  nome_limpo = nome_usuario.strip().lower()
  # Resultado: 'marias2'
  ```
  > **No Banco de Dados:** Sem essa limpeza, o sistema cadastraria `"Maria"`, `"maria "` e `"MARIA"` como três pessoas diferentes!

---

### Slide 3: O Subsumor 2 — A Foto no Escuro e o "Ruído" nos Dados
* **Exemplo do Dia a Dia (Tratamento de Imagem):**
  * Uma foto tirada no escuro fica granulada e com ruído. Antes de postar nos Stories, você aplica filtros e ajusta o brilho.
* **O Análogo em Python:**
  * Imagens são matrizes de números (pixels). Tratar dados é remover discrepâncias (*outliers*) e ruídos para deixar a base nítida e confiável.

---

### Slide 4: O Subsumor 3 — A Planilha do Rolê (Dados Ausentes e Inconsistentes)
* **Exemplo do Dia a Dia:**
  * Você e seus amigos criaram uma lista no WhatsApp para dividir as despesas do churrasco:
    * Lucas: `R$ 50,00`
    * Beatriz: `cinquenta reais`
    * Matheus: *deixou em branco*
    * Gabriel: `-R$ 50,00`
  * **Problema:** Se você tentar somar essa lista na calculadora, ela vai travar porque há texto misturado com número e dados faltando!
* **O Análogo em Python (Pandas):**
  ```python
  import pandas as pd

  # 1. Preenche quem deixou em branco com zero:
  df['Valor'] = df['Valor'].fillna('0.00')

  # 2. Converte texto para número decimal:
  df['Valor_Numerico'] = pd.to_numeric(df['Valor'], errors='coerce')
  ```

---

## 🧠 Síntese do Conceito (Organizador Prévio de Ausubel)

| Situação no Cotidiano | Dado Bruto | Tratamento em Python | Resultado Esperado |
| :--- | :--- | :--- | :--- |
| **Erros de digitação e maiúsculas** | `"  são paulo   "` e `"SAO PAULO"` | `.str.strip().str.lower()` | `"sao paulo"` (Registro padronizado) |
| **Planilha de gastos com vírgulas e vazios** | `"50,00"` e células em branco | `.fillna('0.00')` e `.str.replace(',', '.')` | Números decimais somáveis (Float) |
| **Formulário enviado 2 vezes por ansiedade** | Linhas idênticas na tabela | `df.drop_duplicates()` | Apenas 1 registro por participante |

---

## 🎯 Os 3 Desafios da Oficina

Cada desafio possui sua própria pasta com o arquivo de entrada bruto e deve gerar um arquivo chamado **`tratado.csv`** dentro da respectiva pasta.

---

### 🟢 Desafio 1: A Lista de E-mails do Evento (Nível 1)
* **Pasta:** `desafio1/`
* **Entrada:** `desafio1/emails_brutos.csv`
* **Saída esperada:** `desafio1/tratado.csv`
* **Cenário:** Você recebeu a lista de convidados para um evento de tecnologia. Alguns e-mails vieram com espaços nas pontas, outros em letras maiúsculas e alguns em branco.
* **Resolução passo a passo:**
  ```python
  import pandas as pd

  # 1. Carregar a lista de e-mails
  df = pd.read_csv("desafio1/emails_brutos.csv")

  # 2. Preencher e-mails que ficaram em branco
  df["email"] = df["email"].fillna("email_nao_informado@dominio.com")

  # 3. Remover espaços soltos no início e fim
  df["email"] = df["email"].str.strip()

  # 4. Padronizar tudo em letras minúsculas
  df["email"] = df["email"].str.lower()

  # 5. Salvar a tabela limpa
  df.to_csv("desafio1/tratado.csv", index=False)
  ```

---

### 🟡 Desafio 2: A Planilha do Churrasco (Nível 2)
* **Pasta:** `desafio2/`
* **Entrada:** `desafio2/despesas_churrasco.csv`
* **Saída esperada:** `desafio2/tratado.csv`
* **Cenário:** Lista de compras do churrasco entre amigos. Os valores foram digitados com vírgula (`"145,90"`) e algumas pessoas deixaram em branco. O Python não consegue somar textos com vírgulas!
* **Resolução passo a passo:**
  ```python
  import pandas as pd

  # 1. Carregar as despesas
  df = pd.read_csv("desafio2/despesas_churrasco.csv")

  # 2. Preencher valores não informados com zero
  df["valor"] = df["valor"].fillna("0.00")

  # 3. Substituir vírgula brasileira por ponto decimal
  df["valor"] = df["valor"].astype(str).str.replace(",", ".")

  # 4. Converter texto para número decimal (float)
  df["valor"] = df["valor"].astype(float)

  # Bônus: Agora você pode somar o custo total do churrasco!
  print(f"Total do churrasco: R$ {df['valor'].sum():.2f}")

  # 5. Salvar o arquivo corrigido
  df.to_csv("desafio2/tratado.csv", index=False)
  ```

---

### 🟣 Desafio 3: A Lista de Presença da Oficina (Nível 3)
* **Pasta:** `desafio3/`
* **Entrada:** `desafio3/lista_presenca.csv`
* **Saída esperada:** `desafio3/tratado.csv`
* **Cenário:** No formulário de presença, alguns alunos enviaram 2 vezes por ansiedade e digitaram suas cidades ora em minúsculo (`"são paulo"`), ora em maiúsculo (`"SÃO PAULO"`).
* **Resolução passo a passo:**
  ```python
  import pandas as pd

  # 1. Carregar a lista de presença
  df = pd.read_csv("desafio3/lista_presenca.csv")

  # 2. Padronizar cidades em MAIÚSCULAS e sem espaços nas pontas
  df["cidade"] = df["cidade"].str.strip().str.upper()

  # 3. Padronizar nomes no formato Título (Primeira letra maiúscula)
  df["nome"] = df["nome"].str.strip().str.title()

  # 4. Eliminar os cadastros repetidos
  df = df.drop_duplicates()

  # 5. Salvar a lista oficial de participantes únicos
  df.to_csv("desafio3/tratado.csv", index=False)
  ```

---

## 💻 Como Rodar o Gabarito Oficial

Você pode executar todas as soluções de uma vez através do script `gabarito.py`:

```bash
# Executar o script do gabarito:
python gabarito.py
```
> O script processará os 3 desafios automaticamente e gerará os respectivos arquivos `tratado.csv` em cada pasta.

---

## 🌐 Validador Web Interativo (`validador.html`)

O validador foi projetado para permitir que os alunos testem suas soluções diretamente no navegador, sem complicações de terminal:

1. Dê dois cliques em **`validador.html`** no seu computador (ele abrirá no seu navegador favorito: Chrome, Edge, Firefox).
2. Escolha o desafio que você resolveu (**Desafio 1**, **Desafio 2** ou **Desafio 3**).
3. Arraste o seu arquivo **`tratado.csv`** para a tela.
4. **O que você verá:**
   - 🔄 **Tela de Loading:** Animação de carregamento e inspeção em tempo real.
   - 🟢 **Tela de Sucesso (Verdinho):** Parabéns, checklist verde de validação, cálculo de métricas (total do churrasco ou contagem de alunos únicos) e tabela visual com a amostra dos dados tratados.
   - 🔴 **Tela de Erro (Vermelho):** Aponta exatamente onde estão as inconsistências e dá as dicas de código Python para corrigir.
   - 📖 **Botão "Passo a Passo":** Modal completo com as explicações mastigadas linha por linha de cada desafio.