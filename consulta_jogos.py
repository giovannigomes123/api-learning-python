import requests

# URL da API RAWG
api_url = "https://api.rawg.io/api/games"
# Sua chave de API (substitua pela sua chave real)
api_key = "SUA_CHAVE_API"

# Parâmetros da requisição (nome do jogo e chave de API)
params = {
    "key": api_key,
    "page_size": 5,  # Número de jogos retornados
    "page": 1,       # Página de resultados
}

# Fazer a requisição GET
response = requests.get(api_url, params=params)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    # Processar os dados da resposta
    data = response.json()
    games = data.get("results", [])
    
    for game in games:
        print(f"Título: {game['name']}")
        print(f"Data de Lançamento: {game['released']}")
        print(f"Plataformas: {', '.join([platform['platform']['name'] for platform in game['platforms']])}")
        print("----")
else:
    print("Erro na requisição:", response.status_code)
