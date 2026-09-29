# QA Automatizacija - E2E Selenium Python Framework

Projekat automatizovanog testiranja za web aplikaciju primenom Page Object Model (POM) arhitekture.

## Tehnologije i Biblioteke
- **Python** (Programski jezik)
- **Selenium WebDriver** (Automatizacija pretraživača)
- **Pytest** (Test runner i organizacija testova)
- **Faker** (Generisanje dinamičkih test podataka)
- **pytest-html** (Generisanje HTML izveštaja)

## Struktura Projekta
- `pages/` - Page Object klase sa lokalizatorima i akcijama na stranicama.
- `tests/` - Test fajlovi sa Pytest asercijama.
- `conftest.py` - Fixture-i za pokretanje drajvera, `--headless` opciju i generisanje automatskih screenshot-ova pri padu testova.
- `pytest.ini` - Konfiguracija Pytest markera i opcija.

## Pokretanje Testova

### Standardno pokretanje (sa grafičkim interfejsom):
```bash
python -m pytest --html=report.html --self-contained-html