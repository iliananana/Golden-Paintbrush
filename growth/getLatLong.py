# import requests

# def fetch_photos(species_name, per_page=10):
#     # Replace 'YOUR_API_KEY_HERE' with your actual iNaturalist API key if required
#     headers = {
#         'Authorization': 'Bearer YOUR_API_KEY_HERE'
#     }
    
#     # Step 1: Get the taxon ID for the Golden Indian Paintbrush
#     taxon_search_url = f'https://api.inaturalist.org/v1/taxa?q={species_name}'
#     taxon_response = requests.get(taxon_search_url, headers=headers)
#     taxon_data = taxon_response.json()
    
#     if not taxon_data['results']:
#         print("Species not found.")
#         return []
    
#     taxon_id = taxon_data['results'][0]['id']
    
#     # Step 2: Fetch observations of this species
#     observations_url = f'https://api.inaturalist.org/v1/observations?taxon_id={taxon_id}&per_page={per_page}'
#     observations_response = requests.get(observations_url, headers=headers)
#     observations_data = observations_response.json()
    
#     photo_urls = []
    
#     # Step 3: Extract photo URLs from these observations
#     for observation in observations_data['results']:
#         for photo in observation['photos']:
#             photo_urls.append(photo['url'])
    
#     return photo_urls

# # Example usage
# species_name = 'golden Indian paintbrush'  # Example scientific name, replace with the correct one if different
# photos = fetch_photos(species_name)

# for url in photos:
#     print(url)
