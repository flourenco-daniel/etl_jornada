import requests
from tinydb import TinyDB
from datetime import datetime

def extrair():
    url = 'https://api.coinbase.com/v2/prices/spot'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Erro: Código de status: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None

def transformar(dados_json):
    try:
        valor = dados_json['data']['amount']
        criptomoeda = dados_json['data']['base']
        moeda = dados_json['data']['currency']
        dados_tratados = {
            "valor": valor,
            "criptomoeda": criptomoeda,  # Corrigido aqui
            "moeda": moeda,
            "timestamp": datetime.now().isoformat()
        }
        return dados_tratados
    except (KeyError, TypeError) as e:
        print(f"Erro ao transformar dados: {e}")
        return None

def load(dados_tratados):
    if dados_tratados is not None:
        db = TinyDB('db.json')
        db.insert(dados_tratados)
        print("Deu bom!")
    else:
        print("Dados tratados estão vazios. Nada foi salvo.")

if __name__ == '__main__':
    dados_json = extrair()
    dados_transformados = transformar(dados_json)
    load(dados_transformados)