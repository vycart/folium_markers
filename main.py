import folium

# Latitude, Longitude
LOCATION_DATA = [
    ("41.90093256", "12.48331626"),
    ("41.89018285", "12.49235900"),
    ("41.89868519", "12.47684474"),
    ("41.89454167", "12.48303163"),
    ("41.90226256", "12.45739340"),
    ("41.90269661", "12.46635787"),
    ("41.91071023", "12.47635640"),
    ("41.90266442", "12.49624457")
]

LOCATION_NAMES = [
    "Trevi Fountain",
    "Colosseum",
    "Pantheon",
    "Piazza Venezia",
    "St. Peter’s Square",
    "Mausoleum of Hadrian",
    "Piazza del Popolo",
    "Fountain of the Naiads"
]

if __name__ == '__main__':
    folium_map = folium.Map()

    for cords, name in zip(LOCATION_DATA, LOCATION_NAMES):
        folium.Marker(location=[cords[0], cords[1]],
                      popup=f"Lattitude:<br>{cords[0]}<br>"
                            f"Longitude:<br>{cords[1]}<br>"
                            f"Name:<br>{name}"
                      ).add_to(folium_map)

    south_west_corner = min(LOCATION_DATA)
    north_east_corner = max(LOCATION_DATA)

    folium_map.fit_bounds([south_west_corner, north_east_corner])

    folium_map.save("FoliumMap.html")
