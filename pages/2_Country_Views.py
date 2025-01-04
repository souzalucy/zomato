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
st.set_page_config(page_title='Country Views', layout='wide')

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

def restaurant_statistics_graphs(df, graph_type):
    # Criando a coluna 'Colors_name' que mapeia a cor
    df['colors_name'] = df['rating_color'].apply(lambda x: COLORS.get(x, 'Unknown'))

    # Criando a coluna 'Rating_description' com o significado do rating
    df['rating_description'] = df['colors_name'].apply(lambda x: RATING_MEANING.get(x, 'Desconhecido'))

    if graph_type == 'restaurants':
        # 1. Quantidade de Restaurantes por País
        restaurants_by_country = df.groupby('country_name')['restaurant_id'].nunique().reset_index()
        restaurants_by_country = restaurants_by_country.rename(columns={'restaurant_id': 'restaurant_count'})

        # Adicionar a cor do rating como uma coluna para o gráfico
        restaurants_by_country['rating_color'] = df.groupby('country_name')['rating_color'].first().values
        
        # Gráfico de Restaurantes por País
        fig_restaurants = px.bar(restaurants_by_country,
                                 x='country_name',
                                 y='restaurant_count',
                                 title='Quantidade de Restaurantes por País',
                                 labels={'country_name': 'País', 'restaurant_count': 'Quantidade de Restaurantes'},
                                 color='rating_color',
                                 color_discrete_map=COLORS)

        # Remover a legenda automática do Plotly
        fig_restaurants.update_layout(showlegend=False)

        # Adicionar uma legenda manual no canto superior direito
        fig_restaurants.update_layout(
            annotations=[
                dict(
                    x=1, y=1, xref="paper", yref="paper", 
                    text="Legenda de Rating:", showarrow=False, font=dict(size=14, color="black"),
                    align="left", xanchor="right", yanchor="top"
                ),
                dict(
                    x=1, y=0.95, xref="paper", yref="paper", 
                    text="darkgreen: Excelente (4.5 - 5.0)", showarrow=False, font=dict(size=12),
                    align="left", xanchor="right", yanchor="top"
                ),
                dict(
                    x=1, y=0.90, xref="paper", yref="paper", 
                    text="green: Muito bom (4.0 - 4.5)", showarrow=False, font=dict(size=12),
                    align="left", xanchor="right", yanchor="top"
                ),
                dict(
                    x=1, y=0.85, xref="paper", yref="paper", 
                    text="lightgreen: Bom (3.5 - 4.0)", showarrow=False, font=dict(size=12),
                    align="left", xanchor="right", yanchor="top"
                ),
                dict(
                    x=1, y=0.80, xref="paper", yref="paper", 
                    text="orange: Médio (3.0 - 3.5)", showarrow=False, font=dict(size=12),
                    align="left", xanchor="right", yanchor="top"
                ),
                dict(
                    x=1, y=0.75, xref="paper", yref="paper", 
                    text="red: Ruim (2.5 - 3.0)", showarrow=False, font=dict(size=12),
                    align="left", xanchor="right", yanchor="top"
                ),
                dict(
                    x=1, y=0.70, xref="paper", yref="paper", 
                    text="darkred: Péssimo (1.5 - 2.5)", showarrow=False, font=dict(size=12),
                    align="left", xanchor="right", yanchor="top"
                )
            ]
        )

        return fig_restaurants

    elif graph_type == 'cities':
        # 2. Quantidade de Cidades Registradas por País
        cities_by_country = df.groupby('country_name')['city'].nunique().reset_index()
        cities_by_country = cities_by_country.rename(columns={'city': 'city_count'})

        # Adicionar a cor do rating como uma coluna para o gráfico
        cities_by_country['rating_color'] = df.groupby('country_name')['rating_color'].first().values
        
        # Gráfico de Cidades por País
        fig_cities = px.bar(cities_by_country,
                            x='country_name',
                            y='city_count',
                            title='Quantidade de Cidades Registradas por País',
                            labels={'country_name': 'País', 'city_count': 'Quantidade de Cidades'},
                            color='rating_color',
                            color_discrete_map=COLORS)

        # Remover a legenda automática do Plotly
        fig_cities.update_layout(showlegend=False)

        # Adicionar uma legenda manual no canto superior direito
        fig_cities.update_layout(
            annotations=[
                dict(
                    x=1, y=1, xref="paper", yref="paper", 
                    text="Legenda de Rating:", showarrow=False, font=dict(size=14, color="black"),
                    align="left", xanchor="right", yanchor="top"
                ),
                dict(
                    x=1, y=0.95, xref="paper", yref="paper", 
                    text="darkgreen: Excelente (4.5 - 5.0)", showarrow=False, font=dict(size=12),
                    align="left", xanchor="right", yanchor="top"
                ),
                dict(
                    x=1, y=0.90, xref="paper", yref="paper", 
                    text="green: Muito bom (4.0 - 4.5)", showarrow=False, font=dict(size=12),
                    align="left", xanchor="right", yanchor="top"
                ),
                dict(
                    x=1, y=0.85, xref="paper", yref="paper", 
                    text="lightgreen: Bom (3.5 - 4.0)", showarrow=False, font=dict(size=12),
                    align="left", xanchor="right", yanchor="top"
                ),
                dict(
                    x=1, y=0.80, xref="paper", yref="paper", 
                    text="orange: Médio (3.0 - 3.5)", showarrow=False, font=dict(size=12),
                    align="left", xanchor="right", yanchor="top"
                ),
                dict(
                    x=1, y=0.75, xref="paper", yref="paper", 
                    text="red: Ruim (2.5 - 3.0)", showarrow=False, font=dict(size=12),
                    align="left", xanchor="right", yanchor="top"
                ),
                dict(
                    x=1, y=0.70, xref="paper", yref="paper", 
                    text="darkred: Péssimo (1.5 - 2.5)", showarrow=False, font=dict(size=12),
                    align="left", xanchor="right", yanchor="top"
                )
            ]
        )

        return fig_cities

    else:
        print("Tipo de gráfico inválido. Use 'restaurants' ou 'cities'.")

def calculate_country_statistics(df, metric):
    """
    Calcula estatísticas por país com base na métrica escolhida.

    Parâmetros:
        df (pd.DataFrame): O DataFrame com os dados.
        metric (str): A métrica para calcular ("rating" ou "price").
    
    Retorna:
        pd.DataFrame: Resultado da média por país.
    """
    if metric == 'rating':
        # Média de avaliações por país
        result = df.groupby('country_name')['aggregate_rating'].mean().reset_index(name='average_rating')
        result = result.sort_values(by='average_rating', ascending=False).reset_index(drop=True)  # Ordenando e resetando índices
        return result

    elif metric == 'price':
        # Média de preço para duas pessoas por país
        result = df.groupby('country_name')['average_cost_for_two'].mean().reset_index(name='average_cost_for_two_people')
        result = result.sort_values(by='average_cost_for_two_people', ascending=False).reset_index(drop=True)  # Ordenando e resetando índices
        return result

    else:
        raise ValueError("Métrica inválida. Use 'rating' ou 'price'.")
    
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

st.sidebar.markdown('---')
st.sidebar.markdown('### Powered by Lucy Souza')

# Filtrar o DataFrame com base nos países selecionados
filtered_df = df4[df4['country_name'].isin(selected_countries)]

# Layout principal
tab1, = st.tabs(['Visão Principal'])

with tab1:
    with st.container():
        fig = restaurant_statistics_graphs(filtered_df, graph_type='restaurants')
        st.markdown('#  Restaurantes por País')
        st.plotly_chart( fig, use_container_width=True)

    with st.container():
        fig = restaurant_statistics_graphs(filtered_df, graph_type='cities')
        st.markdown('#  Cidades Registradas por País')
        st.plotly_chart( fig, use_container_width=True)

    with st.container():
        st.title("Médias Gerais")
        col1, col2 = st.columns(2, gap='large')
        with col1:
            media = calculate_country_statistics(filtered_df, 'rating')
            st.write("Média de Avaliações por País", media)

        with col2:
            media = calculate_country_statistics(filtered_df, 'price')
            st.write("Média de Preço para Duas Pessoas por País", media)
        