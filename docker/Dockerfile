FROM python:3.10-slim

WORKDIR /app

# Instalacija Firefox-a i potrebnih alata
RUN apt-get update && apt-get install -y \
    firefox-esr \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Instalacija Geckodriver-a
RUN wget -q https://github.com/mozilla/geckodriver/releases/download/v0.35.0/geckodriver-v0.35.0-linux64.tar.gz \
    && tar -xzf geckodriver-v0.35.0-linux64.tar.gz -C /usr/local/bin \
    && rm geckodriver-v0.35.0-linux64.tar.gz

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .