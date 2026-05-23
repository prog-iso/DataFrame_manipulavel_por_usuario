import pandas as pd
from pathlib import Path

# Abrindo o arquivo, criando um dataframe
arq = Path(__file__).parent / "entrada_do_usuario.csv"
try:
    df = pd.read_csv(arq,sep=";")
except: 
    df = pd.DataFrame(columns=["Nome do cliente","Item","Quantidade de itens comprados","Valor da compra","Data do pedido","Data de entrega"])

# Usuário escreve os pedidos
print("Começamos a mexer com Data Frames, com o usuário interferindo:\n")
nome = input("Escreva o nome de quem fez o pedido: ")
item = input("O que ele(a) comprou? ")
quant = input("Quantos desse item foram comprados: ")
valor = input("Quanto foi a compra em reais? ")
data_pedido = input("Quando o pedido foi feito (escreva a data no modelo D/M/A)? ")
data_entrega = input("Quando deverá ser entregue (escreva a data no modelo D/M/A)? ")

# Criando o Data Frame com os dados da compra
dados_pedido = pd.DataFrame({"Nome do cliente":[nome],
                             "Item":[item],
                             "Quantidade de itens comprados":[quant],
                             "Valor da compra":[valor],
                             "Data do pedido":[data_pedido],
                             "Data de entrega":[data_entrega]})

# Juntando os dados do pedido com o da planilha e organizando a planilha
df = pd.concat([df,dados_pedido],ignore_index=True)
df.sort_values("Data de entrega",inplace=True)
df.reset_index(drop=True,inplace=True)

# Salvando essa nova planilha completa
df.to_csv(path_or_buf = arq, sep=";", index=False)