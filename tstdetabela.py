import pandas as pd


formulario = pd.read_excel(r'\demo.xlsx', sheet_name='Planilha1')

data = {'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', pd.NA]}
df = pd.DataFrame.from_dict(data)

if pd.isnull(df['col_2'][3]): # Verifica se pd.isnull() retornou True
    print('Está vazio.')
else:
    print('Está preenchido.')