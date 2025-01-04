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
st.set_page_config(page_title='City Views', layout='wide')

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

def top_cities_analysis(df, analysis_type):
    """
    Encontra o Top 10 cidades com base no tipo de análise escolhida
    (mais restaurantes ou mais tipos culinários distintos) e gera um gráfico.

    Parâmetros:
        df (pd.DataFrame): O DataFrame com os dados.
        analysis_type (str): Tipo de análise ("restaurants" ou "cuisines").

    Retorna:
        None: Exibe o gráfico no Streamlit.
    """
    if analysis_type == 'restaurants':
        # Contar o número de restaurantes por cidade
        result = (
            df.groupby('city')['restaurant_id']
            .count()
            .reset_index(name='restaurant_count')
            .sort_values(by='restaurant_count', ascending=False)
            .head(10)
        )
        y_axis = "restaurant_count"

    elif analysis_type == 'cuisines':
        # Contar o número de tipos culinários distintos por cidade
        result = (
            df.groupby('city')['cuisines']
            .nunique()
            .reset_index(name='distinct_cuisines_count')
            .sort_values(by='distinct_cuisines_count', ascending=False)
            .head(10)
        )
        y_axis = "distinct_cuisines_count"

    else:
        raise ValueError("Tipo de análise inválido. Use 'restaurants' ou 'cuisines'.")

    # Criar o gráfico com Plotly Express
    fig = px.bar(
        result,
        x='city',
        y=y_axis,
        text=y_axis,
        labels={'city': 'Cidades', y_axis: 'Quantidade'},
        template='plotly_white',
    )
    fig.update_traces(textposition='outside')
    fig.update_layout(
        xaxis_title='Cidades',
        yaxis_title='Quantidade',
        showlegend=False
    )

    # Exibir o gráfico
    return fig

def cities_with_rating_range(df, min_rating, max_rating):
    """
    Cria um gráfico das 5 principais cidades com média de avaliações dentro de um intervalo definido pelo usuário.

    Parâmetros:
        df (pd.DataFrame): O DataFrame com os dados.
        min_rating (float): Avaliação mínima.
        max_rating (float): Avaliação máxima.

    Retorna:
        None: Exibe o gráfico no Streamlit.
    """
    # Agrupar os dados por cidade e calcular a média de avaliação
    filtered_df = (
        df.groupby('city')['aggregate_rating']
        .mean()
        .reset_index(name='average_rating')
    )
    
    # Filtrar pelo intervalo definido pelo usuário
    filtered_df = filtered_df[
        (filtered_df['average_rating'] >= min_rating) &
        (filtered_df['average_rating'] <= max_rating)
    ].sort_values(by='average_rating', ascending=False).head(5)

    if filtered_df.empty:
        st.warning("Nenhuma cidade encontrada no intervalo especificado.")
        return

    # Criar o gráfico com Plotly Express
    fig = px.bar(
        filtered_df,
        x='city',
        y='average_rating',
        text='average_rating',
        labels={'city': 'Cidades', 'average_rating': 'Média de Avaliação'},
        template='plotly_white',
    )
    fig.update_traces(textposition='outside')
    fig.update_layout(
        xaxis_title='Cidades',
        yaxis_title='Média de Avaliação',
        showlegend=False,
        title_x=0.5,
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

# Filtro de países
unique_cities = df4['city'].unique()
selected_cities = st.sidebar.multiselect(
    "Escolha as cidades que deseja visualizar:",
    options=unique_cities,
    default=unique_cities  # Preseleciona todos os países
)

st.sidebar.markdown('---')
st.sidebar.markdown('### Powered by Lucy Souza')

# Filtrar o DataFrame com base nos países selecionados
filtered_df = df4[df4['city'].isin(selected_cities)]

# Layout principal
tab1, = st.tabs(['Visão Principal'])

with tab1:
    with st.container():
        # Gráfico: Top 10 cidades com mais restaurantes na base de dados
        fig = top_cities_analysis(filtered_df, 'restaurants')  # Usar o DataFrame filtrado
        st.markdown('# Top 10 cidades com mais restaurantes na base de dados')
        st.plotly_chart(fig, use_container_width=True)

    with st.container():
        col1, col2 = st.columns(2, gap='large')

        with col1:
            # Gráfico: Cidades com média de avaliações acima de 4
            fig = cities_with_rating_range(filtered_df, 4, 5)  # Usar o DataFrame filtrado
            st.markdown('# Cidades com média de avaliações acima de 4')
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            # Gráfico: Cidades com média de avaliações abaixo de 2.5
            fig = cities_with_rating_range(filtered_df, 0, 2.5)  # Usar o DataFrame filtrado
            st.markdown('# Cidades com média de avaliação abaixo de 2.5')
            st.plotly_chart(fig, use_container_width=True)

    with st.container():
        # Gráfico: Top 10 cidades com mais tipos culinários distintos
        fig = top_cities_analysis(filtered_df, 'cuisines')  # Usar o DataFrame filtrado
        st.markdown('# Top 10 cidades mais restaurantes com tipos culinários distintos')
        st.plotly_chart(fig, use_container_width=True)