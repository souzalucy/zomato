import streamlit as st

st.set_page_config(
    page_title="Fome Zero Growth Dashboard",
    layout="wide",
    page_icon="📊"
)

st.header("Marketplace")

st.sidebar.markdown('# Fome Zero')
st.sidebar.markdown('## O melhor lugar para encontrar seu mais novo restaurante favorito!')
st.sidebar.markdown('''---''')

# Texto de introdução
st.write('# Fome Zero Growth Dashboard')
st.markdown("""
### Growth Dashboard  

O **Growth Dashboard** foi desenvolvido para monitorar e analisar as principais métricas relacionadas aos restaurantes em uma visão integrada e segmentada.  

#### Como navegar neste Growth Dashboard?  

- **Principal Page**:  
  - Visão geral de métricas principais, como número de restaurantes, países, cidades, avaliações e tipos de culinárias disponíveis.  

- **Countries**:  
  - Análise detalhada por país, incluindo insights de localização, densidade de restaurantes, médias de avaliações e custos médios para dois.  

- **City**:  
  - Visão granular por cidade, destacando as cidades com maior concentração de restaurantes e os rankings por avaliações e popularidade.  

- **Cuisines**:  
  - Explore os tipos de culinária oferecidos em cada localidade, identificando as opções mais populares e os padrões de avaliações para diferentes tipos de comida.  

#### Colunas e Métricas Trabalhadas  

Este dashboard é baseado em dados detalhados extraídos das seguintes colunas:  
- **Restaurantes**: `restaurant_id`, `restaurant_name`, `aggregate_rating`, `rating_text`, `votes`.  
- **Localização**: `country_name`, `city`, `latitude`, `longitude`, `address`.  
- **Culinária**: `cuisines`, `average_cost_for_two`, `currency`.  
- **Avaliações**: `rating_color`, `rating_text`, `colors_name`.  

#### Solicitações e Suporte  
Caso precise de ajuda, entre em contato pelo e-mail: [souzalucyg@gmail.com](mailto:souzalucyg@gmail.com)  

#### Explore e Descubra!  
Utilize os filtros disponíveis para visualizar os dados por país, cidade ou tipo de culinária e aproveite para encontrar insights sobre os melhores restaurantes e experiências gastronômicas.  
""")