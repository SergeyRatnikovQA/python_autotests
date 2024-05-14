from common.api.pokemons import PokemonApi
from common.api.trainer import TrainerApi
from common.helper.conf import Credential
from faker import Faker

pokemon = PokemonApi()
trainer = TrainerApi()
fake = Faker()
Faker.seed(10)

# Create Pokemon
payload = {"name": f"{fake.first_name_male()}", "photo": "https://dolnikov.ru/pokemons/albums/001.png"}
response = pokemon.create_pokemon(payload=payload, token=Credential.trainer_token)
id = response.response.json()['id']
print(response.response.json())

# Change name pokemon
payload = {"pokemon_id": id, "name": f"{fake.first_name_male()}", "photo": "https://dolnikov.ru/pokemons/albums/001.png"}
response = pokemon.update_pokemon(payload=payload, token=Credential.trainer_token)
print(response.response.json())


# Add pokemon to pokeball
response = trainer.add_pokeball(pokemon_id=id, token=Credential.trainer_token)
print(response.response.json())

