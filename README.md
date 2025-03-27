# Teste de Transformação de Dados - Rol de Procedimentos e Eventos em Saúde

Este repositório contém um código Python que realiza a extração e transformação de dados a partir de um arquivo PDF do **Anexo I - Rol de Procedimentos e Eventos em Saúde**, conforme o teste solicitado. O código executa as seguintes tarefas:

1. **Extração dos dados** da tabela contida no PDF, abrangendo todas as páginas.
2. **Transformação dos dados**, renomeando as colunas "OD" e "AMB" para suas descrições completas, de acordo com a legenda fornecida.
3. **Armazenamento dos dados** em um arquivo CSV estruturado.
4. **Compactação do arquivo CSV** em um arquivo ZIP, denominado `Teste_{seu_nome}.zip`.

## Funcionalidades

### 1. **Extração dos dados do PDF:**
O código usa a biblioteca `tabula` para ler todas as tabelas do arquivo PDF `Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf` (especificando o intervalo de páginas entre 3 e 181).

### 2. **Transformação dos dados:**
As colunas "OD" e "AMB" são renomeadas para suas descrições completas: 
- "OD" é renomeada para **Odontológica**
- "AMB" é renomeada para **Ambulatorial**

### 3. **Armazenamento em CSV:**
Os dados extraídos e transformados são salvos em um arquivo CSV chamado `tabelas_combinadas.csv`.

### 4. **Compactação do CSV em um arquivo ZIP:**
O arquivo CSV é compactado em um arquivo ZIP chamado `Teste_{seu_nome}.zip`.

## Requisitos

Certifique-se de que você tenha o seguinte instalado em seu ambiente:

- Python 3.x
- Bibliotecas Python:
  - `pandas`
  - `tabula-py`
  - `zipfile` (já incluso no Python)

Você pode instalar as dependências necessárias usando o `pip`:

```bash
pip install pandas tabula-py
