#!/usr/bin/env python3
""" This script will display 151 pokemons for 2 seconds each"""
from requests import get 
from random import choice
from time import sleep
from pprint import pprint
import IPython


def giffing(api):
    print(api['species']['name']) 
    i = 5
    while i > 0:
        IPython.display.Image(api['sprites']['front_default'], width = 250)
        sleep(0.5)
        IPython.display.Image(api['sprites']['back_default'], width = 250)
        sleep(0.5)
        i -= 1

def main():
    pokedex = [ i  for i in range(1,152)]
    while True:
        pokemon = choice(pokedex)
        pokedex.remove(pokemon)
        i_pick_u = get("https://pokeapi.co/api/v2/pokemon/" + str(pokemon)).json()
        sleep(2)
        giffing(i_pick_u)

        
if __name__ == "__main__":
    main()
