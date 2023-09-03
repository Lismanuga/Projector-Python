import telebot
import requests
import json


def searching_gif(api_key, search_key, limit=1):
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

            if data['data']:
                gif_data = data['data'][0]
                gif_url = gif_data['images']['original']['url']
                return gif_url
            else:
                return "No GIFs found."

        else:
            return f"Error: {response.status_code}"

    except Exception as e:
        return str(e)


bot = telebot.TeleBot("YOUR_BOT_API")


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Enter key word:")


api_key = 'YOUR_API'


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    search_result = searching_gif(api_key, message.text, 1)
    bot.send_message(message.chat.id, search_result)


if __name__ == "__main__":
    bot.polling()
