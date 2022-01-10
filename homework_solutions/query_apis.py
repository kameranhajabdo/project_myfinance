
import requests

def animals(number: int) :
    url = "https://zoo-animal-api.herokuapp.com/animals/rand/" + str(number)
    animals = requests.get(url).json()
    names = [x['name'] for x in animals]
    return names

print(animals(4))


def get_coins():
    url = "https://api.coingecko.com/api/v3/coins/list"
    coins = requests.get(url).json()
    return coins

def get_all_names():
    coins = get_coins()
    names = [x["name"] for x in coins]
    return names





def get_symbol_and_name(id: str):
    coins = get_coins()
    for a_coin in coins:
        if a_coin["id"] == id:
            return a_coin["name"] , a_coin["symbol"]


print(get_symbol_and_name("myra-ai"))


requests.get("https://api.nasa.gov/planetary/apod", params={"api_key": "DEMO_KEY"}).json()