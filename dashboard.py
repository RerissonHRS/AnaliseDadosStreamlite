import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

st.set_page_config(page_title="Dashboard", page_icon=":bar_chart:", layout="wide")
st.title("Dashboard Interativo- Exemplo")
st.sidebar.title("Dashboard Controls")

# Craiação de dados de exemplo
np.random.seed(42)
df = pd.DataFrame({
    "Data": pd.date_range(start="2023-01-01", periods=365, freq="D"),
    "Vendas": np.random.randint(100, 1000, size=365),
    "Categoria": np.random.choice(["A", "B", "C"], size=365),
    "Região": np.random.choice(["Norte", "Sul", "Leste", "Oeste"], size=365),
})

# Sidebar para filtros
st.sidebar.header("Filtros")
categoria = st.sidebar.multiselect("Selecionar a região:", options=df["Categoria"].unique(), default=df["Categoria"].unique())
regiao = st.sidebar.multiselect("Selecionar a região:", options=df["Região"].unique(), default=df["Região"].unique())

# Filtragem dos dados
df_filtered = df[(df["Categoria"].isin(categoria)) & (df["Região"].isin(regiao))]

# Layout em colunas
col1, col2 = st.columns(2)

# Gráfico de Barras
with col1:
    st.header("Gráfico de Vendas por Categoria")
    fig = px.bar(df_filtered, x="Categoria", y="Vendas", color="Região", barmode="group")
    st.plotly_chart(fig, use_container_width=True)

# Gráfico de Dispersão
with col2:
    st.header("Gráfico de Dispersão")
    fig = px.scatter(df_filtered, x="Data", y="Vendas", color="Categoria", size="Vendas", hover_name="Região")
    st.plotly_chart(fig, use_container_width=True)

# Gráfico de Linhas
st.header("Gráfico de Linhas")
fig = px.line(df_filtered, x="Data", y="Vendas", color="Categoria", markers=True)
st.plotly_chart(fig, use_container_width=True)

# Métricas 
st.header("Métricas")
col1, col2, col3 = st.columns(3)
col1.metric("Total de Vendas", f"R$ {df_filtered["Vendas"].sum():,.2f}")
col2.metric("Média de Vendas", f"R$ {df_filtered["Vendas"].mean():,.2f}")
col3.metric("Número de Transações", df_filtered.shape[0])

# Tabela de Dados
st.header("Tabela de Dados")
st.dataframe(df_filtered, use_container_width=True)

# Nota sobre interatividade
st.info("Use os filtros na barra lateral para interagir com os dados. Você pode selecionar múltiplas categorias e regiões para visualizar diferentes combinações.")
# Corrigindo o tamanho do DataFrame gerado
df = pd.DataFrame({
    "Data": pd.date_range(start="2023-01-01", periods=365, freq="D"),
    "Vendas": np.random.randint(100, 1000, size=365),
    "Categoria": np.random.choice(["A", "B", "C"], size=365),
    "Região": np.random.choice(["Norte", "Sul", "Leste", "Oeste"], size=365),
})
