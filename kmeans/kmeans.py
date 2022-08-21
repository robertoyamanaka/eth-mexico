from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler  # MinMaxScaler
import pandas as pd
import numpy as np
import sys

sys.path.append("../")
from lunar_crush.lunar_crush import LunarCrushData


# -----------------------------------------------------------
# Aux Functions
# -----------------------------------------------------------


def get_euclidian_distance_to_point(point, df_coords):
    return np.sqrt(np.sum((point - df_coords.iloc[:, 4:]) ** 2, axis=1))


# -----------------------------------------------------------
# Main Pipeline
# -----------------------------------------------------------
def get_coords():
    scaler = StandardScaler()

    df = LunarCrushData.all_data

    # We remain with the numeric columns
    scaled_data = scaler.fit_transform(df.iloc[:, 5:])

    # n_clusters gotten from experimentation
    kmeans_lunar = KMeans(n_clusters=3, random_state=42)
    kmeans_array = kmeans_lunar.fit_transform(scaled_data)

    df_kmeans = pd.DataFrame(kmeans_array, columns=["x_coord", "y_coord", "z_coord"])
    # append the coords found to the tags
    df_coords = pd.concat([df.iloc[:, :4], df_kmeans], axis=1)

    # lets save the kmeans result
    df_coords.to_csv(
        "/Users/robertoyamanaka/Documents/EthHack/eth-mexico/kmeans/kmeans_results.csv",
        index=False,
    )


def get_min_distance_symbol(symbol):
    df_coords = pd.read_csv(
        "/Users/robertoyamanaka/Documents/EthHack/eth-mexico/kmeans/kmeans_results_2.csv"
    )
    point = list(df_coords[df_coords["symbol"]==df_coords].loc[0])[-3:]
    distancias = get_euclidian_distance_to_point(point, df_coords)
    min_distance_pos = np.argmin(distancias)
    return df_coords.iloc[min_distance_pos]["symbol"]
