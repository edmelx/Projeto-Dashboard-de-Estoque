#ETL

import pandas as pd
from sqlalchemy import create_engine

df_prod = pd.read_csv('produtos.csv')
df_movs = pd.read_csv('movimentacoes.csv')

print(f'Produtos carregados: {len(df_prod)}')
print(f'Movimentações carregadas: {len(df_movs)}')

entradas = df_movs[df_movs['tipo'] == 'Entrada'].groupby('id_produto')['quantidade'].sum()

saidas = df_movs[df_movs['tipo'] == 'Saída'].groupby('id_produto')['quantidade'].sum()

df_prod['saldo'] = df_prod['id'].map(entradas).fillna(0) - df_prod['id'].map(saidas).fillna(0)

df_prod['status'] = df_prod.apply(
    lambda r: 'Repor' if r['saldo'] <= r['estoque_minimo'] else 'OK', axis=1)


print(f'Produtos para repor: {len(df_prod[df_prod["status"] == "Repor"])}')
print(f'Produtos OK:         {len(df_prod[df_prod["status"] == "OK"])}')




engine = create_engine('sqlite:///estoque.db')
df_prod.to_sql('produtos',      engine, if_exists='replace', index=False)
df_movs.to_sql('movimentacoes', engine, if_exists='replace', index=False)

df_prod.to_csv('produtos_tratados.csv', index=False)
print('CSV exportado!')

print('ETL conluído!')