import json
import pytest
import requests

# Funkcija koja čita podatke iz našeg JSON fajla
def ucitaj_json_podatke():
    with open("data/test_data.json", "r", encoding="utf-8") as f:
        return json.load(f)

# Pytest preuzima listu iz JSON-a i parametrizuje test
@pytest.mark.parametrize("data", ucitaj_json_podatke())
def test_api_sa_eksternim_podacima(data):
    url = "https://httpbin.org/anything"
    
    # Šaljemo podatke pročitane iz JSON-a
    payload = {"name": data["korisnik"], "role": data["rola"]}
    response = requests.post(url, json=payload)
    
    # Provere (asertacije)
    assert response.status_code == data["ocekivani_status"]
    assert response.json()["json"]["name"] == data["korisnik"]