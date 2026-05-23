import pandas as pd
from pathlib import Path

# Abrindo o arquivo
arq = Path(__file__).parent / "dados_pessoas.csv"
data_frame = pd.read_csv(arq, skipinitialspace = True)

# Verificando se o arquivo foi aberto corretamente
print("Arquivo lido:\n")
print(data_frame)

# Criando um novo data frame
# Poderia colocar mais de uma pessoa na lista, basta cadastrar os dados em ordem nas tuplas
# Ex, em nome colocar: "Nome":["João Pedro","Carlos Alberto"] e asssim por diante
dados_extras = pd.DataFrame({"Nome":["João Pedro"],
                             "Onde mora":["Taguatinga - DF"],
                             "Salário":[6200],
                             "Sexo":["Masculino"]})

# Verificando esse novo data frame
print("\n\nNovo data frame:\n")
print(dados_extras)

# Unindo os dois data frames e criando um novo
dados_totais = pd.concat([data_frame,dados_extras],ignore_index=True)

# Testando o novo data frame
print("\n\nUnindo todos os dados:\n")
print(dados_totais)

# Salvando um novo arquivo com todos os dados
caminho_do_arquivo_novo = Path(__file__).parent / "novos_dados.csv"
dados_totais.to_csv(path_or_buf = caminho_do_arquivo_novo,index=False,sep=";")