import requests

urls = ["https://diabete.streamlit.app", 
        "https://fap3se.streamlit.app"]

for url in urls:
    response = requests.get(url)

    if response.status_code == 200:
        print(f"Conteúdo de {url}:")
        print(response.text)
    else:
        print(f"Erro ao fazer a requisição para {url}: {response.status_code}")
