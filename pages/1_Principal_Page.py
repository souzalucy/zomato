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
st.set_page_config(page_title='Principal Page', layout='wide')

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

def unicos(dataframe, coluna):
    # Retorna valores únicos
    return dataframe[coluna].nunique()

def Country_Maps(df):
    """
    Exibe um mapa com marcadores agrupados em clusters e cores personalizadas por país e rating.
    """
    # Criando o mapa base
    map = folium.Map()

    # Cluster para agrupamento de marcadores
    marker_cluster = MarkerCluster().add_to(map)

    # Adicionando marcadores com cores personalizadas
    for _, row in df.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=f"""
                Restaurante: {row['restaurant_name']}<br>
                País: {row['country_name']}<br>
                Rating: {row['aggregate_rating']} ({row['rating_text']})
            """,
            icon=folium.Icon(color=row['colors_name'], icon_color='white')
        ).add_to(marker_cluster)

    # Renderizando o mapa
    folium_static(map, width=1024, height=600)

@st.cache_data
def convert_df_to_csv(dataframe):
    """Converte o DataFrame em CSV e retorna como bytes."""
    return dataframe.to_csv(index=False).encode('utf-8')

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
unique_countries = df4['country_name'].unique()
selected_countries = st.sidebar.multiselect(
    "Escolha os países que deseja visualizar os restaurantes:",
    options=unique_countries,
    default=unique_countries  # Preseleciona todos os países
)

st.sidebar.header("Download do Dataset")
csv_data = convert_df_to_csv(df4)
st.sidebar.download_button(
    label="Baixar Dataset Tratado",
    data=csv_data,
    file_name="dataset_tratado.csv",
    mime="text/csv"
)

st.sidebar.markdown('---')
st.sidebar.markdown('### Powered by Lucy Souza')

# Filtrar o DataFrame com base nos países selecionados
filtered_df = df4[df4['country_name'].isin(selected_countries)]

# Layout principal
tab1, = st.tabs(['Visão Principal'])

with tab1:
    with st.container():
      st.markdown('# FOME ZERO!')
      st.markdown('## O melhor lugar para encontrar seu mais novo restaurante favorito!')
      st.markdown('### Temos as seguintes marcas dentro da nossa plataforma:')

      st.title("Overall Metrics")
      col1, col2, col3, col4, col5 = st.columns(5, gap='large')

      with col1:
        restaurantes_unicos = unicos(filtered_df, coluna="restaurant_id")
        col1.metric('Restaurantes', restaurantes_unicos)

      with col2:
        paises = unicos(filtered_df, coluna="country_code")
        col2.metric('Países', paises)

      with col3:
        cidades = unicos(filtered_df, coluna="city")
        col3.metric('Cidades', cidades)

      with col4:
        avaliacoes = filtered_df['votes'].sum()
        col4.metric('Avaliações', avaliacoes)

      with col5:
        cuisines = unicos(filtered_df, coluna="cuisines")
        col5.metric('Culinárias', cuisines)

    with st.container():
       Country_Maps(filtered_df)

