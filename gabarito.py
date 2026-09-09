import sys
import pandas as pd

# Garante compatibilidade de acentuação no terminal do Windows
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# ==============================================================================
# OFICINA DE TRATAMENTO DE DADOS (DATA CLEANING) - 1ª AULA
# Gabarito oficial dos 3 desafios práticos
# ==============================================================================

def resolver_desafio_1():
    """
    DESAFIO 1: A Lista de E-mails do Evento (Texto e Nulos)
    - Entrada: desafio1/emails_brutos.csv
    - Saída esperada: desafio1/tratado.csv
    
    Missão:
    1. Preencher e-mails ausentes com 'email_nao_informado@dominio.com'
    2. Remover espaços extras no início e no final (.str.strip())
    3. Padronizar todos os e-mails em letras minúsculas (.str.lower())
    """
    print("--- Resolvendo Desafio 1: E-mails do Evento ---")
    df = pd.read_csv("desafio1/emails_brutos.csv")
    
    # 1. Trata os dados em branco (NaN)
    df["email"] = df["email"].fillna("email_nao_informado@dominio.com")
    
    # 2. Limpa espaços e coloca em minúsculas
    df["email"] = df["email"].str.strip().str.lower()
    
    # 3. Salva o resultado
    df.to_csv("desafio1/tratado.csv", index=False)
    print("[OK] Desafio 1 salvo com sucesso em desafio1/tratado.csv")
    print(df.head())


def resolver_desafio_2():
    """
    DESAFIO 2: A Planilha do Churrasco (Vírgulas e Tipos Numéricos)
    - Entrada: desafio2/despesas_churrasco.csv
    - Saída esperada: desafio2/tratado.csv
    
    Missão:
    1. Preencher despesas não informadas com '0.00' (.fillna('0.00'))
    2. Trocar vírgula brasileira por ponto americano (.str.replace(',', '.'))
    3. Converter os valores para número decimal (.astype(float))
    """
    print("\n--- Resolvendo Desafio 2: Planilha do Churrasco ---")
    df = pd.read_csv("desafio2/despesas_churrasco.csv")
    
    # 1. Preenche quem não colocou valor com 0.00
    df["valor"] = df["valor"].fillna("0.00")
    
    # 2. Substitui vírgula por ponto (para o Python entender como decimal)
    df["valor"] = df["valor"].astype(str).str.replace(",", ".")
    
    # 3. Converte para número decimal (float)
    df["valor"] = df["valor"].astype(float)
    
    # Bônus: Agora podemos somar o total do churrasco!
    total = df["valor"].sum()
    print(f"Total gasto no churrasco: R$ {total:.2f}")
    
    # 4. Salva o resultado
    df.to_csv("desafio2/tratado.csv", index=False)
    print("[OK] Desafio 2 salvo com sucesso em desafio2/tratado.csv")
    print(df.head())


def resolver_desafio_3():
    """
    DESAFIO 3: A Lista de Presença da Oficina (Duplicatas e Padronização)
    - Entrada: desafio3/lista_presenca.csv
    - Saída esperada: desafio3/tratado.csv
    
    Missão:
    1. Padronizar cidades: sem espaços e em letras MAIÚSCULAS (.str.strip().str.upper())
    2. Padronizar nomes: sem espaços e formato Título (.str.strip().str.title())
    3. Eliminar cadastros duplicados (.drop_duplicates())
    """
    print("\n--- Resolvendo Desafio 3: Lista de Presença ---")
    df = pd.read_csv("desafio3/lista_presenca.csv")
    
    # 1. Padroniza a coluna cidade
    df["cidade"] = df["cidade"].str.strip().str.upper()
    
    # 2. Padroniza a coluna nome
    df["nome"] = df["nome"].str.strip().str.title()
    
    # 3. Remove alunos repetidos (que enviaram formulário 2x)
    total_antes = len(df)
    df = df.drop_duplicates()
    total_depois = len(df)
    print(f"Linhas antes: {total_antes} | Alunos únicos após remoção de duplicatas: {total_depois}")
    
    # 4. Salva o resultado
    df.to_csv("desafio3/tratado.csv", index=False)
    print("[OK] Desafio 3 salvo com sucesso em desafio3/tratado.csv")
    print(df.head())


if __name__ == "__main__":
    resolver_desafio_1()
    resolver_desafio_2()
    resolver_desafio_3()
    print("\n[SUCESSO] Todos os 3 desafios foram resolvidos com sucesso!")
