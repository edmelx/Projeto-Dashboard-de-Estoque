# gera dados.py
import pandas as pd, random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker('pt_BR')
random.seed(42)

# categorias e tipo de movimentação
categorias = ['Eletrônicos', 'Alimentos', 'Limpeza', 'Escritório']
tipos = ['Entrada', 'Saída']

# gerar 20 produtos fictícios
produtos = []
for i in range(1, 21):
    produtos.append({
        'id': i,
        'nome': f'Produto {i:03d}',
        'categoria': random.choice(categorias),
        'estoque_minimo': random.randint(5, 20)
    })
pd.DataFrame(produtos).to_csv('produtos.csv', index=False)

# gera 300 movimentações no estoque

movs = []
for i in range(1, 301):
    movs.append({
        'id': i,
        'id_produto':random.randint(1, 20),
        'tipo': random.choice(tipos),
        'quantidade': random.randint(1, 50),
        'data': fake.date_between('-90d', 'today').strftime('%Y-%m-%d')
    })
pd.DataFrame(movs).to_csv('movimentos.csv', index=False)

print('Dados gerados com sucesso!')
