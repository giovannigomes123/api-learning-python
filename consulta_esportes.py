import requests

# URL da API The Sports DB
api_url = "https://www.thesportsdb.com/api/v1/json/1/searchteams.php"
# Parâmetros da requisição (nome do time e chave de API)
params = {
    "t": "Manchester United",  # Substitua pelo nome do time desejado
}

# Fazer a requisição GET
response = requests.get(api_url, params=params)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    # Processar os dados da resposta
    data = response.json()
    teams = data.get("teams", [])
    
    for team in teams:
        print(f"Nome do Time: {team['strTeam']}")
        print(f"Estádio: {team['strStadium']}")
        print(f"Treinador: {team['strManager']}")
        print("----")
else:
    print("Erro na requisição:", response.status_code)
