import geopandas as gpd

# Charger le GeoJSON
gdf = gpd.read_file("ICU_clean-source.json")

# Reprojeter vers WGS84
gdf = gdf.to_crs(epsg=4326)

# Sauvegarder un nouveau fichier GeoJSON compatible D3
gdf.to_file("ICU_clean_geoWGS84.json", driver="GeoJSON")