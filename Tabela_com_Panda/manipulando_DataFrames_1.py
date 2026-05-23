import pandas as pd
from pathlib import Path

# Abrindo o arquivo e criando um data frame
arq = Path(__file__).parent / "novos_dados.csv"
df = pd.read_csv(arq,sep=";")

# Testando se deu certo
print("Começando o teste de manipulação:\n\nAbrindo o data frame:\n")
print(df)

# Removendo um nome desse data frame e testando se deu certo
# Eu opitei por tirar um nome, mas poderia tirar todo mundo que ganhasse menos de 5000
# ex: df = df[df["Salário"] >= 5000]
df = df[df["Nome"] != "Henrique Almeida"]

print("\n\nRemovendo um nome:\n")
print(df)

# Ordenando as pessoas com base no salário e testando se deu certo
# Poderia ter colocado ascending = True (mas é opicional, porque, se nâo botar, é setado para True)
df.sort_values("Salário",inplace=True)

print("\n\nOrdenando as pessoas com base no salário (de modo crescente):\n")
print(df)

# Arrumando o index e testando
df.reset_index(drop=True,inplace=True)

print("\n\nAgora, temos o índice re-arrumado:\n")
print(df)

# Criando um novo arquivo com um dado a menos e uma nova ordem
arq_new = Path(__file__).parent / "dados_reordenados.csv"
df.to_csv(path_or_buf = arq_new, index=False, sep = ";")