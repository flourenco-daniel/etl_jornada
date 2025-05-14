from sqlalchemy import create_engine, Column, String, Float, Integer, DateTime #pra criar o schema
from sqlalchemy.orm import declarative_base, sessionmaker #pra fazer os inserts e updates
from datetime import datetime
from time import sleep
import requests


DATABASE_URL = "postgresql://admin:S8tC8CFAd67f5URTGbc1FOtGSur9bgPS@dpg-d0hu322dbo4c7386eeng-a.oregon-postgres.render.com/postges_pjps"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class BitcoinDados(Base):
    __tablename__ = "bitcoin_dados"

    id = Column(Integer, primary_key=True)
    valor = Column(Float)
    criptomoeda = Column(String(10))
    moeda = Column(String(10))
    timestamp = Column(DateTime)

Base.metadata.create_all(engine)

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

def transformar(dados_extraidos):
    try:
        valor = dados_extraidos['data']['amount']
        criptomoeda = dados_extraidos['data']['base']
        moeda = dados_extraidos['data']['currency']
        dados_tratados = BitcoinDados(
            valor = valor,
            criptomoeda = criptomoeda,
            moeda = moeda,
            timestamp=datetime.now()
        )
        return dados_tratados
    except (KeyError, TypeError) as e:
        print(f"Erro ao transformar dados: {e}")
        return None
    

def salvar_dados_sqlalchemy(dados):
    with Session() as session:
        session.add(dados)
        session.commit()
        print("Dados salvos no psql")

if __name__ == "__main__":
    while True:
        dados_extraidos = extrair()
        dados_tratados = transformar(dados_extraidos)

        print("Dados tratados:")
        print(dados_tratados.__dict__)

        salvar_dados_sqlalchemy(dados_tratados)

        print("Aguardando 15 segundos")
        sleep(15)


