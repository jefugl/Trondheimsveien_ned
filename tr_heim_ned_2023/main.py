import folium
import pandas


def main():
    data = pandas.read_csv("trondheimsveien.txt")
    lat = list(data["lat"])
    lon = list(data["lon"])
    nm = list(data["name"])
    adr = list(data["adresse"])

    start = 59.928, 10.778
    kart = folium.Map(location=start, zoom_start=14, tiles="OpenStreetMap")

    fg = folium.FeatureGroup(name="My Map")

    for lt, ln, nm, adr in zip(lat, lon, nm, adr):
        nope = str(nm)
        fg.add_child(folium.Marker(location=[lt, ln], popup=f"{nm}\n{adr}",
                                   icon=folium.Icon(icon="beer", prefix="fa", color="red")))
        kart.add_child(fg)

    kart.save("index.html")


if __name__ == "__main__":
    main()
