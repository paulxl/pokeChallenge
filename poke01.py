#!/usr/bin/env python3

# imports always go at the top of your code
import requests

def lookUp(userChoice):

    pokeapi = requests.get(f"https://pokeapi.co/api/v2/pokemon/{userChoice}").json()

    print("name : ",pokeapi["species"]["name"])
    print("here is a link to its front image:  ",pokeapi["sprites"]["front_default"])
    print("it was in this many game indices: ", len(pokeapi["game_indices"]))
    pokeMoves = []
    #numOfMoves = len(pokeapi["moves"])
    for dict in pokeapi["moves"]:
        pokeMoves.append(dict["move"]["name"])

    print("here is a list of its moves: ", pokeMoves)


def main():
    print("This is a pokemon search tool")
    print("Give me a number from 1 to 150 and I will look it up for you ")
    while True:
        try:
            userChoice = int(input("> ").strip())
            if userChoice < 1 and userChoice > 150:
                print("error number not within bounds")
                break
            else:
                lookUp(userChoice)
            break
        except ValueError:
            print("invalid entry not a number")


main()