import requests

# URL da API Spotify
api_url = "https://api.spotify.com/v1/search"
# Sua chave de API (substitua pela sua chave real)
access_token = "SUA_CHAVE_DE_ACESSO"

# Parâmetros da requisição (termo de pesquisa)
params = {
    "q": "Adele",  # Substitua pelo termo desejado
    "type": "artist",  # Tipo de pesquisa (artista, álbum, faixa, etc.)
    "limit": 5  # Número de resultados retornados
}

# Cabeçalhos da requisição
headers = {
    "Authorization": f"Bearer {access_token}"
}

# Fazer a requisição GET
response = requests.get(api_url, headers=headers, params=params)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    # Processar os dados da resposta
    data = response.json()
    artists = data.get("artists", {}).get("items", [])
    
    for artist in artists:
        print(f"Nome do Artista: {artist['name']}")
        print(f"Popularidade: {artist['popularity']}")
        print(f"Seguidores: {artist['followers']['total']}")
        print("----")
else:
    print("Erro na requisição:", response.status_code)
