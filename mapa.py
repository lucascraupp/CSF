import folium
from folium.plugins import HeatMap
import pandas as pd


def cria_mapa(df: pd.DataFrame, nome_mapa, zoom, radius, centro):

    # Criar um mapa com base em uma localização inicial
    mapa = folium.Map(location=centro, zoom_start=zoom)

    # Lista de coordenadas de latitude e longitude
    coordenadas = []

    # Extrair coordenadas do JSON
    i = 0
    for indice, dado in df.iterrows():
        lat = dado['Lat']
        lon = dado['Long']
        pot = (dado['RSSI']-df['RSSI'].min()) / \
            (df['RSSI'].max() - df['RSSI'].min())
        coordenadas.append([lat, lon, pot])
        i += 1

    # Criação do objeto HeatMap com as coordenadas
    heatmap = HeatMap(coordenadas,min_opacity=0.3, blur=1, radius=radius, gradient={
        '0.2': 'deepskyblue',
        '0.4': 'aqua',
        '0.6': 'lime',
        '0.8': 'gold',
        '0.9': 'orange',
        '1.0': 'red'
    })
    # Adicionar o mapa de calor ao mapa
    heatmap.add_to(mapa)

    # Salvar o mapa em um arquivo HTML
    mapa.save(f'{nome_mapa}.html')
