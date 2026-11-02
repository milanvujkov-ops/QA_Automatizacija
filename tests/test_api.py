import pytest
import requests

def test_get_users():
    # Koristimo httpbin za pouzdan GET zahtev
    url = "https://httpbin.org/get"
    
    response = requests.get(url)
    
    # Proveravamo da li je status 200 OK
    assert response.status_code == 200, f"Izgubili smo vezu, status je: {response.status_code}"
    
    data = response.json()
    
    # Proveravamo da li odgovor sadrži url ključ
    assert "url" in data
    print("\n[INFO] GET zahtev uspešno prošao!")

def test_create_user():
    # Koristimo httpbin za POST zahtev
    url = "https://httpbin.org/post"
    
    new_user_data = {
        "name": "Novi Korisnik",
        "username": "novi.korisnik",
        "email": "novi.korisnik@test.com",
        "website": "testcorp.io"
    }
    
    response = requests.post(url, json=new_user_data)
    
    # httpbin za POST vraća status 200
    assert response.status_code == 200, f"Neočekivan status kod: {response.status_code}"
    
    response_data = response.json()
    
    # Proveravamo poslate podatke
    assert response_data["json"]["name"] == "Novi Korisnik"
    assert response_data["json"]["email"] == "novi.korisnik@test.com"
    
    print("\n[INFO] POST zahtev uspešan! Podaci uspešno poslati na server.")

    # Definisali smo listu korisnika koje testiramo
@pytest.mark.parametrize("ime, korisnicko_ime, email", [
    ("Milan Nikolić", "milan_qa", "milan@test.com"),
    ("Ana Petrović", "ana_dev", "ana@test.com"),
    ("Stefan Jovanović", "stefan_test", "stefan@test.com")
])
def test_create_multiple_users(ime, korisnicko_ime, email):
    # ⚠️ OVDE JE FALILA OVA LINIJA KOJA DEFINIŠE URL:
    url = "https://httpbin.org/post"
    
    user_data = {
        "name": ime,
        "username": korisnicko_ime,
        "email": email
    }
    
    response = requests.post(url, json=user_data)
    
    # Proveravamo da je zahtev uspešan (status 200)
    assert response.status_code == 200, f"Greška za korisnika {ime}"
    
    response_data = response.json()
    
    # Proveravamo vraćene podatke
    assert response_data["json"]["name"] == ime
    assert response_data["json"]["email"] == email
    
    print(f"\n[INFO] Uspešno testiran korisnik: {ime}")


def test_error_status_code():
    url = "https://httpbin.org/status/400"
    
    response = requests.post(url)
    
    assert response.status_code == 400, f"Očekivali smo grešku 400, a dobili status: {response.status_code}"
    
    print("\n[INFO] Test greške uspešno prošao! Server je ispravno vratio status 400.")
    
@pytest.fixture
def uzorak_novog_korisnika():
    # Fixture priprema podatke unapred
    podaci = {
        "name": "Milan Fixture",
        "username": "milan_f",
        "email": "milan.fixture@test.com"
    }
    print("\n[INFO] Fixture je pripremio test podatke!")
    return podaci

def test_sa_fixture_podacima(uzorak_novog_korisnika):
    url = "https://httpbin.org/post"
    
    # Test direktno uzima pripremljene podatke iz fixture-a
    response = requests.post(url, json=uzorak_novog_korisnika)
    
    assert response.status_code == 200
    
    response_data = response.json()
    assert response_data["json"]["name"] == uzorak_novog_korisnika["name"]
    print("[INFO] Test sa fixture-om je uspešno prošao!")