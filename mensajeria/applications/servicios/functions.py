import requests

import requests

def get_lat_long_google(address, city, country, department, api_key):
    full_address = f"{address}, {city}, {department}, {country}"
    geocoding_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={full_address}&key={api_key}"
    
    # Imprimir la URL para depuración
    print(f"URL de geocodificación: {geocoding_url}")
    
    response = requests.get(geocoding_url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Imprimir la respuesta JSON para depuración
        print(f"Respuesta JSON: {data}")
        
        if data['results']:
            location = data['results'][0]['geometry']['location']
            return location['lat'], location['lng']
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
    
    return None, None

# Ejemplo de uso
address = "carrera 12 # 52 - 46"
city = "Santiago de Cali"
country = "Colombia"
department = "Valle del Cauca"
api_key = 'AIzaSyDIsLYWRxE2ME1PBLk1ugSZvu8OLfoAuKE'  # Reemplaza con tu clave API

latitude, longitude = get_lat_long_google(address, city, country, department, api_key)
print(f"Latitud: {latitude}, Longitud: {longitude}")


def get_lat_long_osm(address, city, country, department):
    full_address = f"{address}, {city}, {department}, {country}"
    geocoding_url = f"https://nominatim.openstreetmap.org/search?format=json&q={full_address}"
    response = requests.get(geocoding_url)
    
    if response.status_code == 200:
        data = response.json()
        if data:
            location = data[0]
            return float(location['lat']), float(location['lon'])
    return None, None

# Ejemplo de uso
address = "Cra 12 #52 - 46"
city = "Santiago de cali"
country = "Colombia"
department = "Valle del cauca"

latitude, longitude = get_lat_long_osm(address, city, country, department)
print(f"Latitud: {latitude}, Longitud: {longitude}")
