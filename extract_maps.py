import osmnx as ox

# Définir la zone Bordeaux Métropole
place_name = "Bordeaux Métropole, France"

# Types de routes à récupérer (grands axes)
highway_types = ["motorway", "trunk", "primary"]

# Construire le filtre OSMnx pour ces types
custom_filter = '[\"highway\"~\"{}\"]'.format("|".join(highway_types))

# Télécharger le graphe routier filtré
G = ox.graph_from_place(place_name, network_type='drive', custom_filter=custom_filter)

# Convertir en GeoDataFrame des arêtes (routes)
edges = ox.graph_to_gdfs(G, nodes=False, edges=True)

# Retirer les colonnes qui posent problème à l’écriture GeoJSON
for col in edges.columns:
    if edges[col].dtype == 'O':  # objet Python, souvent des listes ou dicts
        edges[col] = edges[col].astype(str)

# Sauvegarder en GeoJSON
edges.to_file("axes_principaux.geojson", driver="GeoJSON")

print("✅ Fichier 'axes_principaux.geojson' généré.")
