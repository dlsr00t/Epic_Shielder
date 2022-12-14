import pandas as pd

nome = 'Douglas'
sheet_Pessoas = pd.read_excel("test.xlsx", sheet_name=0)
sheet_Clientes = pd.read_excel("test.xlsx", sheet_name=1)
sheet_Pessoas.loc[-1] = [nome]  

with pd.ExcelWriter("test.xlsx", mode='a') as writer:
    sheet_Pessoas.to_excel(writer, sheet_name = 'Sheet1', index = False)
