import pandas as pd
import os
import glob

def resolver_desafio_1():
    print("Resolvendo Desafio 1...")
    df = pd.read_csv("desafio1/bcdata.sgs.22784.csv", sep=";")
    
    # 1. Substituir vírgula por ponto
    df["valor"] = df["valor"].str.replace(",", ".")
    
    # 2. Converter para float
    df["valor"] = df["valor"].astype(float)
    
    # 3. Converter data para datetime (opcional, mas recomendado)
    df["data"] = pd.to_datetime(df["data"], format="%d/%m/%Y")
    
    # 4. Salvar
    df.to_csv("desafio1/tratado.csv", index=False)
    print("Desafio 1 salvo em desafio1/tratado.csv")

def resolver_desafio_2():
    print("Resolvendo Desafio 2...")
    try:
        # Requer odfpy instalado (pip install odfpy)
        df = pd.read_excel("desafio2/CargosVagosVacancias_202607.ods", engine="odf")
        
        # 1. Limpar nomes das colunas (tudo minúsculo, substituir espaços por _)
        # Padronização clássica
        df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_").str.replace(r"[^\w\s]", "", regex=True)
        
        # 2. Remover nulos (Dropna em linhas que são totalmente vazias)
        df = df.dropna(how="all")
        
        # Preencher nulos nas demais com 0
        df = df.fillna(0)
        
        # Salvar
        df.to_csv("desafio2/tratado.csv", index=False)
        print("Desafio 2 salvo em desafio2/tratado.csv")
    except Exception as e:
        print(f"Não foi possível resolver o desafio 2. Verifique se tem odfpy instalado. Erro: {e}")

def resolver_desafio_3():
    print("Resolvendo Desafio 3...")
    
    # Encontrar todos os arquivos .p7s
    arquivos = glob.glob("desafio3/*.p7s")
    
    dados = []
    
    for arquivo in arquivos:
        nome_arquivo = os.path.basename(arquivo)
        
        # Extrair o nome do remetente do nome do arquivo (ex: Hash-Remetente1-carlos.p7s)
        partes = nome_arquivo.replace(".p7s", "").split("-")
        remetente = partes[-1] if len(partes) > 1 else "desconhecido"
        
        try:
            with open(arquivo, "rb") as f:
                conteudo = f.read()
                
            # Aqui simulamos a extração de um hash (pegando os primeiros 20 caracteres hexadecimais como exemplo)
            hash_extraido = conteudo.hex()[:20] if conteudo else "vazio"
            
            dados.append({
                "arquivo_origem": nome_arquivo,
                "remetente": remetente,
                "hash": hash_extraido
            })
            
        except Exception as e:
            print(f"Erro ao ler {arquivo}: {e}")
            
    # Criar DataFrame
    df = pd.DataFrame(dados)
    
    # Remover duplicatas
    df = df.drop_duplicates()
    
    # Salvar
    df.to_csv("desafio3/tratado.csv", index=False)
    print("Desafio 3 salvo em desafio3/tratado.csv")

if __name__ == "__main__":
    resolver_desafio_1()
    resolver_desafio_2()
    resolver_desafio_3()
    print("Todos os gabaritos gerados!")
