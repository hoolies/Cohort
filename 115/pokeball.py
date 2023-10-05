#!/usr/bin/env python3

import requests
from random import choice
from time import sleep

def main():
    pokedex = [ i  for i in range(1,152)]
    while True:
        pokemon = choice(pokedex)
        pokedex.remove(pokemon)
        i_pick_u = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(pokemon)).json()
        sleep(2)
        print(i_pick_u)
        
if __name__ == "__main__":
    main()
