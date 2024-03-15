import os
import django
import requests
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from backend.backend.models import Stock, StockData

def fetch_apple_stock_data():
    with open('apikey.txt', 'r') as file:
        api_key = file.read().strip()
        
    response = requests.get('https://www.alphavantage.co/query', params={
        'function': 'TIME_SERIES_DAILY',
        'symbol': 'AAPL',
        'apikey': api_key,
    })

    data = response.json()

    stock, created = Stock.objects.get_or_create(symbol='AAPL')

    for date, values in data['Time Series (Daily)'].items():
        StockData.objects.create(
            stock=stock,
            date=datetime.strptime(date, '%Y-%m-%d').date(),
            open=values['1. open'],
            high=values['2. high'],
            low=values['3. low'],
            close=values['4. close'],
            volume=values['5. volume'],
        )

fetch_apple_stock_data()