import folium
from folium.plugins import HeatMap
import pandas as pd
import math

# Função para gerar as coordenadas
def gerar_coordenadas(coordenada_base, direcao, distancia_total, distancia_entre_pontos):
    coordenadas = []
    lat_base, lon_base = coordenada_base
    distancia_atual = 0

    while distancia_atual <= distancia_total:
        distancia_lat = distancia_atual * math.cos(math.radians(direcao))
        distancia_lon = distancia_atual * math.sin(math.radians(direcao))

        nova_lat = lat_base + (distancia_lat / 111111)
        nova_lon = lon_base + (distancia_lon / (111111 * math.cos(math.radians(lat_base))))

        coordenadas.append((nova_lat, nova_lon))

        distancia_atual += distancia_entre_pontos

    return coordenadas


# Parâmetros de entrada
coordenada_base = (-27.60795022, -48.63369853)  # Coordenada base (latitude, longitude)
direcao = 65 # Direção em graus (0 = norte, 90 = leste, 180 = sul, 270 = oeste)
distancia_total = 8000 # Distância total a percorrer a partir da coordenada base (em metros)
distancia_entre_pontos = 500  # Distância entre cada ponto gerado (em metros)
angulo_abertura = 60  # Ângulo de abertura em graus

# Converter o ângulo de abertura para radianos
angulo_abertura_rad = math.radians(angulo_abertura)

# Calcular as coordenadas limite do mapa de calor
lat_base, lon_base = coordenada_base
lat_norte = lat_base + (distancia_total / 111111) * math.cos(angulo_abertura_rad / 2)
lon_leste = lon_base + (distancia_total / 111111) * math.sin(angulo_abertura_rad / 2)
lat_sul = lat_base - (distancia_total / 111111)
lon_oeste = lon_base - (distancia_total / 111111)

# Gerar as coordenadas
coordenadas = gerar_coordenadas(coordenada_base, direcao, distancia_total, distancia_entre_pontos)

# Criar o DataFrame das coordenadas
df = pd.DataFrame(coordenadas, columns=['Latitude', 'Longitude'])

# Filtrar as coordenadas dentro do ângulo de abertura
df_filtrado = df[(df['Latitude'] <= lat_norte) & (df['Longitude'] <= lon_leste) & (df['Latitude'] >= lat_sul) & (df['Longitude'] >= lon_oeste)]

# Criar o mapa de calor com folium
mapa = folium.Map(location=coordenada_base, zoom_start=13)

# Adicionar o mapa de calor
HeatMap(data=df_filtrado[['Latitude', 'Longitude']].values, radius=10, min_opacity=0.1).add_to(mapa)

# Salvar o mapa como arquivo HTML
mapa.save('mapa_de_calor.html')