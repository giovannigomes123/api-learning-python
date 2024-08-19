import requests

# URL da API OMDb
api_url = "http://www.omdbapi.com/"
# Sua chave de API (substitua pela sua chave real)
api_key = "44ec7412"

# Parâmetros da requisição (título do filme e chave de API)
params = {
    "t": "Avengers endgame",  # Substitua pelo título do filme desejado
    "apikey": api_key
}

# Fazer a requisição GET
response = requests.get(api_url, params=params)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    # Processar os dados da resposta
    data = response.json()
    title = data.get("Title", "N/A")
    year = data.get("Year", "N/A")
    director = data.get("Director", "N/A")
    plot = data.get("Plot", "N/A")

    # Exibir os dados
    print(f"Título: {title}")
    print(f"Ano: {year}")
    print(f"Diretor: {director}")
    print(f"Sinopse: {plot}")
else:
    print("Erro na requisição:", response.status_code)
