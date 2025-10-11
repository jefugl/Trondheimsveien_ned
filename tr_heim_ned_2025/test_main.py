import folium

def main():
    # Startposisjon
    start = [59.9282, 10.7821]

    # HTML direkte i popup (uten IFrame)
    html = """
    <img src='IMG_0481.jpg' width='150' height='113'><br>
    <strong>Renna Pub</strong><br>
    Trondheimsveien 100
    """

    # Lag kart
    m = folium.Map(location=start, zoom_start=15)

    # Lag popup direkte
    popup = folium.Popup(html, max_width=250)

    # Legg til én markør
    folium.Marker(
        location=start,
        popup=popup,
        icon=folium.Icon(icon="beer", prefix="fa", color="blue")
    ).add_to(m)

    # Lagre HTML
    m.save("index.html")

if __name__ == "__main__":
    main()