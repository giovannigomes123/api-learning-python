import requests

# URL da API Google Books
api_url = "https://www.googleapis.com/books/v1/volumes"
# Parâmetros da requisição (termo de pesquisa)
params = {
    "q": "Harry Potter",  # Substitua pelo termo desejado
    "maxResults": 5       # Número de livros retornados
}

# Fazer a requisição GET
response = requests.get(api_url, params=params)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    # Processar os dados da resposta
    data = response.json()
    books = data.get("items", [])
    
    for book in books:
        title = book.get("volumeInfo", {}).get("title", "N/A")
        authors = ", ".join(book.get("volumeInfo", {}).get("authors", ["N/A"]))
        print(f"Título: {title}")
        print(f"Autores: {authors}")
        print("----")
else:
    print("Erro na requisição:", response.status_code)
