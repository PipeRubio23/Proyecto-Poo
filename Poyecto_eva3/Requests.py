import requests
from beautifultable import BeautifulTable
import json
import os

def requestPokemon(): 
    table = BeautifulTable()
    table.columns.header = ["N° Pokedex","Nombre","Altura","Peso","Tipo 1","Tipo 2"]

    tipos = []
 
    id = input("Ingrese El ID del Pokemon: ")
    respuesta =  requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
    if respuesta.status_code == 200:
        pokemon = respuesta.json()

        for x in pokemon['types']:
            tipos.append(x['type']['name'])
        
        if len(tipos)>1:
            table.rows.append([pokemon['id'],pokemon['name'],pokemon['height'],pokemon['weight'], tipos[0], tipos[1]])
            print(table)
            lista = ({"id" : pokemon['id'],"Nombre" :pokemon['name'],"Altura" :pokemon['height'],"Peso" :pokemon['weight'],"Tipo 1" : tipos[0], "Tipo 2" : tipos[1]})

        else:
            table.rows.append([pokemon['id'],pokemon['name'],pokemon['height'],pokemon['weight'], tipos[0], "-------"])
            print(table)
            lista = ({"id" : pokemon['id'],"Nombre" :pokemon['name'],"Altura" :pokemon['height'],"Peso" :pokemon['weight'],"Tipo 1" : tipos[0], "Tipo 2" : "-------"})

        if not os.path.exists("pokedex.json"):
            pokedex = []
        else:
            with open("pokedex.json", "r") as archivo:  
                pokedex = json.load(archivo)


        pokedex.append(lista)

        with open("pokedex.json", "w") as archivo:
            json.dump(pokedex, archivo, indent=4)
        print("Guardado")
              
    else:
        print("Error, Pokemon No Encontrado")
