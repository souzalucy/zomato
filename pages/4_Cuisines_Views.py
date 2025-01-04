# -*- coding: utf-8 -*-

# Importação de bibliotecas
import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
from PIL import Image
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static
import re

# Configuração inicial do Streamlit
st.set_page_config(page_title='Cuisines Views', layout='wide')

# Funções
def rename_columns(dataframe):
    # Renomeia colunas
    renamed_dataframe = dataframe.copy()

    # Funções de transformação para as colunas
    title = lambda x: x.title()
    snakecase = lambda x: re.sub(r'([a-z])([A-Z])', r'\1_\2', x).lower().replace(" ", "_")
    spaces = lambda x: x.replace(" ", "")

    cols_old = [title(str(x)) for x in renamed_dataframe.columns]
    cols_old = [spaces(x) for x in cols_old]
    cols_new = [snakecase(x) for x in cols_old]

    renamed_dataframe.columns = cols_new
    return renamed_dataframe

def best_restaurants_by_cuisine(df, top_n_cuisines=5):
    """
    Encontra os melhores restaurantes com base na avaliação agregada
    para os tipos culinários mais populares.

    Parâmetros:
        df (pd.DataFrame): O DataFrame com os dados.
        top_n_cuisines (int): O número de tipos culinários mais populares a considerar.

    Retorna:
        pd.DataFrame: DataFrame com os melhores restaurantes por tipo culinário.
    """
    # Contar a quantidade de restaurantes por tipo culinário
    cuisine_counts = (
        df['cuisines']
        .value_counts()
        .head(top_n_cuisines)
        .index
    )

    # Filtrar apenas os tipos culinários mais populares
    popular_cuisines_df = df[df['cuisines'].isin(cuisine_counts)]

    # Encontrar os melhores restaurantes (maior avaliação) por tipo culinário
    best_restaurants = (
        popular_cuisines_df.loc[popular_cuisines_df.groupby('cuisines')['aggregate_rating'].idxmax()]
    )

    # Selecionar colunas relevantes
    result = best_restaurants[
        ['restaurant_name', 'cuisines', 'aggregate_rating', 'city', 'country_name']
    ].sort_values(by='aggregate_rating', ascending=False)

    return result

def top_10_restaurants(df):
    """
    Função para encontrar os top 10 restaurantes com maior média de avaliação (aggregate_rating).
    
    Parâmetros:
        df (pd.DataFrame): O DataFrame com os dados de restaurantes.
    
    Retorna:
        pd.DataFrame: DataFrame com os top 10 restaurantes por avaliação.
    """
    # Ordenar o DataFrame pela coluna 'aggregate_rating' em ordem decrescente
    top_10_df = df.sort_values(by='aggregate_rating', ascending=False).head(10)
    
    # Selecionando colunas relevantes para exibir
    top_10_df = top_10_df[['restaurant_name', 'country_name', 'city', 'aggregate_rating']]
    
    return top_10_df

def top_10_cuisines_by_rating(df, top_or_bottom='top'):
    """
    Calcula os 10 melhores ou 10 piores tipos culinários com base na média de avaliação (aggregate_rating)
    e gera um gráfico de barras usando Plotly Express.
    
    Parâmetros:
        df (pd.DataFrame): O DataFrame com os dados de restaurantes.
        top_or_bottom (str): Se 'top', retorna os 10 melhores tipos culinários. Se 'bottom', retorna os 10 piores.
    
    Retorna:
        fig: Gráfico de barras Plotly.
    """
    # Agrupar por tipo de culinária e calcular a média de aggregate_rating
    cuisine_rating = df.groupby('cuisines')['aggregate_rating'].mean().reset_index()
    
    # Ordenar os valores com base na média de aggregate_rating
    if top_or_bottom == 'top':
        top_10 = cuisine_rating.sort_values(by='aggregate_rating', ascending=False).head(10)
    elif top_or_bottom == 'bottom':
        top_10 = cuisine_rating.sort_values(by='aggregate_rating', ascending=True).head(10)
    else:
        raise ValueError("O parâmetro 'top_or_bottom' deve ser 'top' ou 'bottom'")
    
    # Criar o gráfico de barras com Plotly Express
    fig = px.bar(
        top_10,
        x='cuisines', 
        y='aggregate_rating',
        title=f'Top 10 Tipos Culinários - { "Melhores" if top_or_bottom == "top" else "Piores" } Avaliações',
        labels={'cuisines': 'Tipo de Culinária', 'aggregate_rating': 'Média de Avaliação'},
        color='aggregate_rating',
        color_continuous_scale='Viridis'
    )
    
    # Exibir o gráfico
    return fig

# Importando dados
df = pd.read_csv("zomato.csv")
df1 = df.dropna()

# Configurações iniciais
COUNTRIES = {
    1: "India",
    14: "Australia",
    30: "Brazil",
    37: "Canada",
    94: "Indonesia",
    148: "New Zealand",
    162: "Philippines",
    166: "Qatar",
    184: "Singapore",
    189: "South Africa",
    191: "Sri Lanka",
    208: "Turkey",
    214: "United Arab Emirates",
    215: "England",
    216: "United States of America"
}
df1['country_name'] = df1['Country Code'].apply(lambda x: COUNTRIES.get(x, 'Unknown'))

COLORS = {
    "3F7E00": 'darkgreen',
    "5BA829": 'green',
    "9ACD32": 'lightgreen',
    "CDD614": 'orange',
    "FFBA00": 'red',
    "CBCBC8": 'darkred',
    "FF7800": 'darkred'
}
df1['Colors_name'] = df1['Rating color'].apply(lambda x: COLORS.get(x, 'Unknown'))

# Definindo as cores e seus significados de rating
RATING_MEANING = {
    "darkgreen": "Excelente (4.5 - 5.0)",
    "green": "Muito bom (4.0 - 4.5)",
    "lightgreen": "Bom (3.5 - 4.0)",
    "orange": "Médio (3.0 - 3.5)",
    "red": "Ruim (2.5 - 3.0)",
    "darkred": "Péssimo (1.5 - 2.5)",
    "Unknown": "Desconhecido"
}

# Criando a coluna 'Rating_description' baseada na 'Colors_name'
df1['Rating_description'] = df1['Colors_name'].apply(lambda x: RATING_MEANING.get(x, 'Desconhecido'))

df2 = rename_columns(df1)
df2['cuisines'] = df2.loc[:, "cuisines"].apply(lambda x: x.split(",")[0])
df3 = df2.drop('switch_to_order_menu', axis=1)
df4 = df3.drop_duplicates()

# Barra lateral
st.sidebar.markdown('# FOME ZERO!')
st.sidebar.markdown('---')

# 1. Filtro de países
unique_countries = df4['country_name'].unique()
selected_countries = st.sidebar.multiselect(
    "Escolha os países que deseja visualizar os restaurantes:",
    options=unique_countries,
    default=unique_countries  # Preseleciona todos os países
)

# 2. Caixa de seleção para o tipo de culinária
unique_cuisines = df4['cuisines'].dropna().unique()
cuisine_selected = st.sidebar.multiselect(
    "Escolha o tipo de culinária",
    options=unique_cuisines,
    default=['Home-made', 'BBQ', 'Japanese', 'Brazilian', 'Arabian', 'American', 'Italian']  # Preseleciona todos os países
)

st.sidebar.markdown('---')
st.sidebar.markdown('### Powered by Lucy Souza')

# Filtrar o DataFrame com base nos países selecionados
filtered_df_country = df4[df4['country_name'].isin(selected_countries)]

# Filtro para o tipo de culinária selecionado
filtered_df_cuisines = df4[df4['cuisines'].isin(cuisine_selected)]

# Layout principal
tab1, = st.tabs(['Visão Principal'])

with tab1:
    with st.container():
        melhor = best_restaurants_by_cuisine(filtered_df_cuisines, top_n_cuisines=5)
        st.write("# Melhores restaurantes dos principais tipos culinários", melhor)

    with st.container():
        top = top_10_restaurants(filtered_df_country)
        st.write("# Top 10 restaurantes e culinárias", top)

    with st.container():
        fig = top_10_cuisines_by_rating(filtered_df_cuisines, top_or_bottom='top')
        st.plotly_chart( fig, use_container_width=True)

    with st.container():
        fig = top_10_cuisines_by_rating(filtered_df_cuisines, top_or_bottom='bottom')
        st.plotly_chart( fig, use_container_width=True)