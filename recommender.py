from sklearn.neighbors import NearestNeighbors
import pandas as pd
import numpy as np


def n_neighbors_url_map_dest(start, distance_types, test_feat):
    df_routes = pd.read_csv("data/routes_dataset.csv")
    map_feats = ["difficulty", "scenery"]
    distance_types_data = df_routes[(df_routes["distance_type"]==distance_types) & (df_routes["starting_point"] == start)]

    neigh = NearestNeighbors()
    neigh.fit(distance_types_data[map_feats].to_numpy())

    n_neighbors = neigh.kneighbors([test_feat], n_neighbors=len(distance_types_data), return_distance=False)[0]

    route_coordinates = distance_types_data.iloc[n_neighbors]["route_coordinate (lat,lon)"].tolist()
    distance = distance_types_data.iloc[n_neighbors]["distance (m)"].tolist()
    duration = distance_types_data.iloc[n_neighbors]["duration (s)"].tolist()
    name = distance_types_data.iloc[n_neighbors]["name"].tolist()
    return route_coordinates, distance, duration, name

def recommend_destination(start, distance_types, difficulty, scenery):
    test_feat = [difficulty, scenery]
    route_coordinates, distance, duration, name = n_neighbors_url_map_dest(start, distance_types, test_feat)
    return route_coordinates[0:3], distance, duration, name