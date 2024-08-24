import folium

# Koordinat Makassar
latitude, longitude = -5.147665, 119.432732

# Buat peta dengan lokasi awal di Makassar
map_center = [latitude, longitude]
mymap = folium.Map(location=map_center, zoom_start=12, tiles='OpenStreetMap')

# Tambahkan lapisan satelit dari Google Maps
folium.TileLayer(
    tiles='https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', 
    attr='Google',
    name='Google Satellite',
    overlay=True,
    control=True
).add_to(mymap)

# Tambahkan titik koordinat Makassar
folium.Marker([latitude, longitude], popup='Makassar').add_to(mymap)

# Tambahkan kontrol layer
folium.LayerControl().add_to(mymap)

# Simpan peta sebagai file HTML
mymap.save("makassar_map.html")

# Untuk menampilkan peta dalam notebook Jupyter, gunakan:
mymap
