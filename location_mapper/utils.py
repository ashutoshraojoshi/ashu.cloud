def extract_coordinates_from_google_maps_url(google_maps_url):
    # Find the position of "@" and "/data" in the URL
    at_position = google_maps_url.find("@")
    data_position = google_maps_url.find("/data")

    

    # Check if both "@" and "/data" are found in the URL
    if at_position != -1 and data_position != -1:
        # Extract the substring between "@" and "/data"
        coordinates_str = google_maps_url[at_position + 1:data_position]
        list = coordinates_str.split(",")


        return list
