import requests
from tinydb import TinyDB
from datetime import datetime



def extrair():
    url = 'https://api.coinbase.com/v2/prices/spot'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return(response.json())
        else:
            return(f"Erro: Código de status: {response.status_code}")
    except requests.exception.RequestException as e:
            return(f"Erro na requisição: {e}")

extrair()


def transformar(dados_json):
    try:
        valor = dados_json['data']['amount']
        criptomoeda = dados_json['data']['base']
        moeda = dados_json['data']['currency']
        dados_tratados = {
            "valor": valor,
            "criptomoeda:": criptomoeda,
            "moeda": moeda,
            "timestamp": datetime.now().isoformat()
        }
        return dados_tratados
    except KeyError as e:
        print(f"Erro: Chave ausente no JSON: {e}")
        return None

def load(dados_tratados):
    db = TinyDB('db.json')
    db.insert(dados_tratados)
    print("Deu bom!")

if __name__ == '__main__':
    dados_json = extrair()
    dados_transformados = transformar(dados_json)
    load(dados_transformados)
