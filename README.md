# Análise do Dataset da API Zomato
## 1. Sobre o Dataset
O Dataset da API Zomato é um recurso valioso para os amantes da gastronomia (foodies) que desejam explorar e experimentar as melhores culinárias de restaurantes ao redor do mundo. Este dataset fornece informações valiosas sobre os restaurantes mais bem avaliados em várias cidades, ajudando os usuários a tomar decisões informadas sobre onde comer com base em fatores como nome do restaurante, tipo de culinária, avaliações e mais.

Os dados são atualizados automaticamente toda semana para garantir que os foodies tenham acesso aos restaurantes mais recentes e bem avaliados em suas respectivas cidades. Isso é especialmente útil para aqueles que desejam descobrir novos locais para comer ou planejar aventuras gastronômicas.

Limitações: O dataset é baseado na extração do nível gratuito da API Zomato, que permite buscar apenas os 100 melhores restaurantes por cidade.

## 2. Colunas do Dataset
O dataset normalmente contém as seguintes colunas relacionadas às informações dos restaurantes:

*restaurant_id*: Identificador único de cada restaurante.
*restaurant_name*: Nome do restaurante.
*country_code*: Código do país onde o restaurante está localizado.
*city*: Cidade onde o restaurante está localizado.
*address*: Endereço do restaurante.
*locality*: Área local ou bairro do restaurante.
*longitude*: Coordenada de longitude do restaurante.
*latitude*: Coordenada de latitude do restaurante.
*cuisines*: Tipos de culinária servidos pelo restaurante.
*average_cost_for_two*: Custo médio de uma refeição para duas pessoas.
*currency*: Moeda utilizada no restaurante.
*has_table_booking*: Disponibilidade de reserva de mesa no restaurante.
*has_online_delivery*: Se o restaurante oferece entrega online.
*is_delivering_now*: Se o restaurante está entregando no momento.
*price_range*: Faixa de preço no restaurante (geralmente um número que indica a acessibilidade).
*aggregate_rating*: Avaliação geral do restaurante.
*rating_color*: Código de cor que representa a avaliação do restaurante.
*rating_text*: Descrição do rating (por exemplo, "Excelente", "Bom").
*votes*: Número de votos dos usuários recebidos pelo restaurante.
*country_name*: Nome do país onde o restaurante está localizado.
*colors_name*: Nome associado ao código de cor da avaliação.

## 3. Exploração dos Dados
Com esse dataset, você pode explorar os principais restaurantes das cidades baseando-se em vários parâmetros, como:

Tipos de culinária: Descubra restaurantes que servem diferentes tipos de culinária em várias cidades.
Avaliações: Analise os restaurantes com as melhores ou piores avaliações.
Análise baseada na localização: Visualize a distribuição dos melhores restaurantes em várias cidades e países.

## 4. Problemas de negócios
O dataset da API Zomato pode ser utilizado para:

Recomendações de restaurantes: Ajudar usuários a encontrar os melhores restaurantes nas suas cidades ou de suas culinárias favoritas.
Análise de tendências de mercado: Compreender quais cidades possuem o maior número de restaurantes populares.
Turismo gastronômico: Planejar viagens gastronômicas com base nos dados de restaurantes mais bem avaliados.
Inteligência de negócios: Ajudar donos de restaurantes ou profissionais de marketing a analisar o desempenho de competidores e tendências na indústria de alimentos.

## 5. Estratégia da solução
### 5.1 Perguntas de negócios
#### Visão geral
1. Quantos restaurantes únicos estão registrados?
2. Quantos países únicos estão registrados?
3. Quantas cidades únicas estão registradas?
4. Qual o total de avaliações feitas?
5. Qual o total de tipos de culinária registrados?

#### Visão País
1. Qual o nome do país que possui mais cidades registradas?
2. Qual o nome do país que possui mais restaurantes registrados?
3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4 registrados?
4. Qual o nome do país que possui a maior quantidade de tipos de culinária distintos?
5. Qual o nome do país que possui a maior quantidade de avaliações feitas?
6. Qual o nome do país que possui a maior quantidade de restaurantes que fazem entrega?
7. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam reservas?
8. Qual o nome do país que possui, na média, a maior quantidade de avaliações registrada?
9. Qual o nome do país que possui, na média, a maior nota média registrada?
10. Qual o nome do país que possui, na média, a menor nota média registrada?
11. Qual a média de preço de um prato para dois por país?

#### Visão Cidade
1. Qual o nome da cidade que possui mais restaurantes registrados?
2. Qual o nome da cidade que possui mais restaurantes com nota média acima de 4?
3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de 2.5?
4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?
5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária distintas?
6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem reservas?
7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem entregas?
8. Qual o nome da cidade que possui a maior quantidade de restaurantes que aceitam pedidos online?

#### Visão Restaurantes
1. Qual o nome do restaurante que possui a maior quantidade de avaliações?
2. Qual o nome do restaurante com a maior nota média?
3. Qual o nome do restaurante que possui o maior valor de uma prato para duas pessoas?
4. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor média de avaliação?
5. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que possui a maior média de avaliação?
6. Os restaurantes que aceitam pedido online são também, na média, os restaurantes que mais possuem avaliações registradas?
7. Os restaurantes que fazem reservas são também, na média, os restaurantes que possuem o maior valor médio de um prato para duas pessoas?
8. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América possuem um valor médio de prato para duas pessoas maior que as churrascarias americanas (BBQ)?

#### Visão Tipos de Culinária
1. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a maior média de avaliação?
2. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a menor média de avaliação?
3. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a maior média de avaliação?
4. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a menor média de avaliação?
5. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a maior média de avaliação?
6. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a menor média de avaliação?
7. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a maior média de avaliação?
8. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a menor média de avaliação?
9. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a maior média de avaliação?
10. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a menor média de avaliação?
11. Qual o tipo de culinária que possui o maior valor médio de um prato para duas pessoas?
12. Qual o tipo de culinária que possui a maior nota média?
13. Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos online e fazem entregas?

Os códigos resposta, em python, das perguntas a cima podem ser encontradas no arquivo: perguntas_de_negocios.ipynb.

### 5.2 Dashboard
O painel estratégico foi desenvolvido utilizando as métricas que refletem as 4 principais visões do modelo de negócio da empresa:

- Visão geral
- Visão dos países envolvidos
- Visão das cidades envolvidas
- Visão dos tipos de culinárias envolvidas

Cada visão é representada pelo seguinte conjunto de métricas.
1. Visão geral
Overall Metrics (a. Restaurantes, b. Países, c. Cidades, d. Avaliações, e. Culinárias), além de um mapa para georeferenciamento dos restaurantes e suas notas atribuídas.
   
2. Visão dos países envolvidos
a. Quantidade de restaurantes por país, b. Cidades registradas por país, c. Médias gerais (média de avaliações por país e média de preço para duas pessoas por país).

3. Visão das cidades envolvidas
a. Top 10 cidades com mais restaurantes na base de dados, b. Cidades com média de avaliações acima de 4, c. Cidades com média de avaliação abaixo de 2.5, d. Top 10 cidades mais restaurantes com tipos culinários distintos.

4. Visão dos tipos de culinárias envolvidas
a. Melhores restaurantes dos principais tipos culinários, b. Top 10 restaurantes e culinárias, c. Top 10 tipos culinários (melhores e piores avaliações)

Painel online, hospedado em um Cloud e disponível para acesso em qualquer dispositivo conectado à internet.

## O painel pode ser acessado através desse link: https://zomato2024.streamlit.app/

# 6. Conclusão
O Dataset da API Zomato é uma ferramenta valiosa para explorar o mundo gastronômico, oferecendo informações detalhadas sobre os melhores restaurantes, suas avaliações e características em várias cidades ao redor do mundo. Com dados atualizados semanalmente, é possível acompanhar as tendências do setor, descobrir novas opções de restaurantes e analisar o desempenho de diferentes tipos de culinária em diversas regiões.

Este dataset se torna especialmente útil para quem deseja planejar viagens gastronômicas, recomendar restaurantes, ou ainda para profissionais de marketing e donos de restaurantes que desejam entender o cenário competitivo e as preferências dos consumidores. Com análises de avaliação, custo médio por refeição, tipos de culinária e outros parâmetros, é possível tomar decisões informadas sobre onde e o que comer, além de entender melhor o panorama global dos restaurantes.

O painel estratégico desenvolvido com base nesse dataset oferece uma visão clara e abrangente sobre a distribuição geográfica, as avaliações dos restaurantes, as preferências culinárias e as tendências do mercado, proporcionando uma forma eficaz de monitorar e explorar os dados.

Com isso, o dataset não apenas serve para a análise de dados, mas também como uma excelente ferramenta para consumidores e profissionais da indústria de alimentos que buscam aperfeiçoar suas decisões e estratégias no mercado gastronômico.
