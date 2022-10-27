import requests
def CEP (cep):
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/') #.get puxa a info de uma url
    print(response.status_code) #se printar 200, existe. 400 não existe .status_code me dá a resposta se existe ou não.
    print(response.json())
    print(type(response.json())) #json é de tipo dictionary
    # print(response.text) # .text mostra todo o conteúdo do html
    dados_cep = response.json()
    print(dados_cep['uf'])
    return dados_cep
def POKEMON (pokemon_name):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}/')
    print(response.status_code)
    dado_poke = response.json()
    print(dado_poke['sprites'] ['front_shiny'], "Essa é a sprite do shiny" ) #me manda o link do sprite de um pokemonzin
def site (url): #pega o texto de um site que eu colocar
    response = requests.get(url)
    texto = response.text #pega o texto do site
    return texto
if __name__ == '__main__':
   
    POKEMON(pokemon_name= input("Qual o nome do Pokemon que você deseja? ")
