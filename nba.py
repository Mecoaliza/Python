# Captar os dados via reqsição
from requests import get

BASE_URL = "http://data.nba.net"    # Váriavel global que posso usar ao longo do script
ALL_JSON = "/prod/v1/today.json"

def get_links():
    response = get(BASE_URL+ALL_JSON).json()
    return response ["links"]

def get_currentScoreboard():
    response = get(BASE_URL+get_links()["currentScoreboard"]).json()
    return response

print(get_currentScoreboard())