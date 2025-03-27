
import pandas as pd
import tabula
from zipfile import ZipFile

# Ler tabelas apenas a partir da página 3-181
dfs = tabula.read_pdf("Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf", pages="3-181")

# Concatenar todas as tabelas em um único DataFrame
df_completo = pd.concat(dfs, ignore_index=True)

#Trocando o nome das colunas
df_completo.rename(columns={'OD':'Odontológica', 'AMB': 'Ambulatorial'}, inplace=True)

# Selecionar as 13 primeiras colunas
colunas_desejadas = df_completo.columns[:13]  # Pega as 13 primeiras colunas
df_filtrado = df_completo[colunas_desejadas]

# Salvar o DataFrame no formato CSV
df_filtrado.to_csv('tabelas_combinadas.csv', index=False)

# Nome do arquivo CSV gerado
csv_filename = 'tabelas_combinadas.csv'
# Nome do arquivo ZIP
zip_filename = 'tabelas_combinadas.zip'

# Criar o arquivo ZIP e adicionar o CSV
with ZipFile(zip_filename, 'w') as zipf:
    zipf.write(csv_filename, arcname=csv_filename)  # Adiciona o CSV ao arquivo ZIP


print('Finalizado com sucesso!')
