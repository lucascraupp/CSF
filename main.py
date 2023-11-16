import os

import numpy as np
import pandas as pd

from calculo_perda import perda_caminho
from mapa import cria_mapa

basedir = os.path.abspath(os.path.dirname(__file__))
PotTx = 13.89


def coleta_dados(path):
    files = os.listdir(f"{basedir}/{path}")

    df_list = []
    for file in files:
        if file.endswith(".csv"):
            df = pd.read_csv(f"{basedir}/{path}/{file}")
            df = df.groupby("Date and Time").first()
            df["Nome"] = file[:-4]
            df_list.append(df)

    df_coord = pd.read_json("./data/coordenadas.json")

    df_total = pd.DataFrame(columns=["Nome", "RSSI", "Distc", "Lat", "Long"])

    for df in df_list:
        df_teste = pd.DataFrame()
        df_teste["Distc"] = df_coord["distancia"].loc[
            df_coord["local"] == df["Nome"][0]
        ]
        df_teste["Lat"] = df_coord["latitude"].loc[df_coord["local"] == df["Nome"][0]]
        df_teste["Long"] = df_coord["longitude"].loc[df_coord["local"] == df["Nome"][0]]
        df_teste["Nome"] = df["Nome"][0]
        df_teste["RSSI"] = df["rssi"].mean()
        df_teste["std"] = df["rssi"].std()
        df_teste["Pl"] = PotTx - df["rssi"].mean()
        df_total = pd.concat([df_total, df_teste])

    df_total.reset_index(inplace=True, drop=True)
    print(df_total.head(100))
    return df_total


def processa_dados(df: pd.DataFrame, d0, rssi_0):
    parametro = perda_caminho(
        distancias=df["Distc"].to_list(),
        perdas=df["RSSI"].to_list(),
        d0=d0,
        pl_d0=rssi_0,
    )
    return parametro


df_outdoor = coleta_dados("data/outdoor")

parametro_outdoor = processa_dados(df_outdoor, 407.45, -77.800000)

print(parametro_outdoor)


cria_mapa(
    df=df_outdoor,
    nome_mapa="mapa_outdoor",
    zoom=15,
    radius=30,
    centro=[-27.606824, -48.623519],
)
