import pandas as pd

df = pd.read_excel("clientes.xlsx")  
clientes = {}

for _, row in df.iterrows():
    clientes[str(row["cpf"])] = {
        "nome": row["nome"],
        "endereco": row["endereco"],
        "plano": row["plano"]
    }
