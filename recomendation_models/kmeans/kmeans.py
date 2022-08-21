from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler  # MinMaxScaler
import pandas as pd
import numpy as np
import sys

sys.path.append("../")
from kmeans.lunar_crush import LunarCrushData


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


def get_min_distance_symbol(symbol, df_coords, symbol_json_20):
    try:
        point = df_coords[df_coords["symbol"] == symbol][
            ["x_coord", "y_coord", "z_coord"]
        ].values[0]
    except:
        raise Exception("Symbol not found")
        point = [0, 0, 0]
    df_coords_reduced = df_coords[df_coords["symbol"].isin(list(symbol_json_20.keys()))]
    distancias = get_euclidian_distance_to_point(point, df_coords_reduced)
    distancias = list(filter(lambda score: score > 0.01, distancias))
    min_distance_pos = np.argmin(distancias)
    return (
        df_coords_reduced.iloc[min_distance_pos]["symbol"],
        distancias[min_distance_pos],
    )
