
import requests
import json


def searching_gif(api_key, search_key, limit):
    base_url = "https://api.giphy.com/v1/gifs/search"
    params = {
        'api_key': api_key,
        'q': search_key,
        'limit': limit
    }

    try:
        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            data = json.loads(response.text)

            for gif_data in data['data']:
                gif_url = gif_data['images']['original']['url']
                print(gif_url)
        else:
            print(f"Error: {response.status_code}")

    except Exception as e:
        print(f"{str(e)}")


with open('api_key.txt', 'r') as file:
    api_key = file.read()
search_gif = input("Введіть слово для пошуку: ")
searching_gif(api_key, search_gif, 1)
