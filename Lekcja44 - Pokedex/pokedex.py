import requests
from bs4 import BeautifulSoup
from fpdf import FPDF

def scrap_pokemon_list():
    url = "https://pokemondb.net/pokedex/game/lets-go-pikachu-eevee"
    response = requests.get(url)
    # print(response.content)
    soup = BeautifulSoup(response.content, 'html.parser')
    pokemons_list = []
    cards_list = soup.find('div', class_ = 'infocard-list')
    cards_data = cards_list.find_all('span', class_ = 'infocard-lg-data')

    for data in cards_data:
        pokemon_name = data.find('a')
        pokemon_no = data.find("small")
        pokemon = (pokemon_name.get_text(), pokemon_no.get_text())
        pokemons_list.append(pokemon)
        print(pokemon)

    return pokemons_list

def get_pokemon_info(pokemon_name: str):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    return response.json()

def get_pokemon_image(pokemon_info):
    link = pokemon_info['sprites']['front_default']
    return link

def get_pokemon_types(pokemon_info):
    types = []
    for item in pokemon_info["types"]:
        type_ = item["type"]["name"]
        types.append(type_)
    return types


pokemons_list = scrap_pokemon_list()
# print(get_pokemon_info("Pikachu"))

for pokemon in pokemons_list:
    try:
        pokemon_info = get_pokemon_info(pokemon[0])
        image_url = get_pokemon_image(pokemon_info)
        img_data = requests.get(image_url).content
        poke_types = get_pokemon_types(pokemon_info)
    except:
        print(pokemon[0])