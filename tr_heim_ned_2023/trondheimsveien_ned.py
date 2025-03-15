import folium
from branca.element import Figure
import pandas


def main():
    data = pandas.read_csv("trondheimsveien.txt")
    lat = list(data["lat"])
    lon = list(data["lon"])
    nm = list(data["name"])
    adr = list(data["adresse"])

    start = 59.928, 10.782

    fig = Figure(width=650, height=350)
    m1 = folium.Map(width=650, height=550, location=start, zoom_start=14, min_zoom=10, max_zoom=18)

    fg = folium.FeatureGroup(name="My Map")

    for lt, ln, nm, adr in zip(lat, lon, nm, adr):
        fg.add_child(folium.Marker(location=[lt, ln], popup=f"{nm}\n{adr}",
                                   icon=folium.Icon(icon="beer", prefix="fa", color="red")))
        m1.add_child(fg)

    fig.add_child(m1)

    folium.TileLayer('Stamen Terrain').add_to(m1)
    folium.TileLayer('Stamen Toner').add_to(m1)
    folium.TileLayer('Stamen Water Color').add_to(m1)
    folium.TileLayer('cartodbpositron').add_to(m1)
    folium.TileLayer('cartodbdark_matter').add_to(m1)
    folium.LayerControl().add_to(m1)

    m1.save("trondheimsveien-ned.html")


if __name__ == "__main__":
    main()
