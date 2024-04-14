import requests

api_url_categories = 'https://api.escuelajs.co/api/v1/categories'

def get_requests():
    response = requests.get(api_url_categories)
    categories = response.json()
    for category in categories:
        print(category['name'])