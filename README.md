# Projeto-Dashboard-de-Estoque
Um projeto de um dashboard básico de estoque


# 📦 Controle de Estoque

Pipeline de dados simulando o controle de estoque de uma empresa.

## 🛠️ Tecnologias utilizadas
- Python (pandas, faker, sqlalchemy)
- SQLite
- Power BI Desktop

## 📋 Etapas do projeto
1. **Geração dos dados** — 20 produtos e 300 movimentações fictícias geradas com Python
2. **ETL** — cálculo de saldo por produto e classificação de status
3. **Dashboard** — visualização no Power BI com KPIs e gráficos

## 📊 Dashboard
- **Total de Produtos** — quantidade total de produtos cadastrados
- **Produtos OK** — produtos com saldo acima do estoque mínimo
- **Produtos para Repor** — produtos com saldo abaixo do estoque mínimo
- **Saldo Total** — soma de todos os saldos
- **Saldo por Categoria** — comparativo entre Eletrônicos, Alimentos, Limpeza e Escritório
- **Distribuição por Status** — proporção de produtos OK vs Repor

## 💡 Insights
- Eletrônicos está com saldo negativo — saídas superaram as entradas no período
- 55% dos produtos precisam de reposição — indica alto giro de estoque

## ⚠️ Observação
Projeto desenvolvido para portfólio durante estudos de análise de dados.
Dados fictícios gerados com Python para fins de demonstração.
