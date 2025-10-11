import inputdata
import folium
import pandas as pd
import os

def main():
    start = [59.9282, 10.7821]

    data = pd.DataFrame({
        "nr": inputdata.nr,
        "lat": inputdata.latitude,
        "lon": inputdata.longitude,
        "name": inputdata.pubname,
        "addr": inputdata.pubaddress,
        "img": inputdata.pubimages
    })

    m = folium.Map(location=start, width=650, height=550, zoom_start=14, in_zoom=10, max_zoom=18)

    for i in range(len(data)):
        img_path = data.iloc[i]["img"]
        if os.path.exists(img_path):
            img_html = f"<img src='{img_path}' width='150' height='113'>"
        else:
            img_html = "<div style='color:red;'>Bilde mangler</div>"

        html = f"""
        <div>
            {img_html}<br>
            <strong>{data.iloc[i]['name']}</strong><br>
            {data.iloc[i]['addr']}
        </div>
        """

        popup = folium.Popup(html, max_width=250)

        folium.Marker(
            location=[data.iloc[i]["lat"], data.iloc[i]["lon"]],
            popup=popup,
            icon=folium.Icon(icon="beer", prefix="fa", color="blue")
        ).add_to(m)

    m.save("index.html")

if __name__ == "__main__":
    main()