import requests

url = 'https://api.coinbase.com/v2/prices/spot'


# Define the parameters for the request
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Erro: Código de status: {response.status_code}")
except requests.exception.RequestException as e:
        print(f"Erro na requisição: {e}")
