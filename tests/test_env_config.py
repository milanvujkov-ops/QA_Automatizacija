import os
import pytest
import requests
from dotenv import load_dotenv

# Učitavamo promenljive iz .env fajla
load_dotenv()

def test_api_sa_env_podacima():
    # Čitamo vrednosti iz okruženja
    base_url = os.getenv("BASE_URL")
    user = os.getenv("TEST_USER")
    role = os.getenv("TEST_ROLE")
    
    url = f"{base_url}/anything"
    payload = {"name": user, "role": role}
    
    response = requests.post(url, json=payload)
    
    # Provere
    assert response.status_code == 200
    assert response.json()["json"]["name"] == user