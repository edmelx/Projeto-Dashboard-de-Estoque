# debug.py
import pandas as pd

df_prod = pd.read_csv('produtos.csv')
df_movs = pd.read_csv('movimentacoes.csv')

entradas = df_movs[df_movs['tipo'] == 'Entrada'].groupby('id_produto')['quantidade'].sum()
saidas   = df_movs[df_movs['tipo'] == 'Saida'].groupby('id_produto')['quantidade'].sum()

df_prod['saldo'] = df_prod['id'].map(entradas).fillna(0) - df_prod['id'].map(saidas).fillna(0)

print(df_prod[['id', 'nome', 'estoque_minimo', 'saldo']].head(10))