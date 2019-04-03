import requests
import json

from django.shortcuts import render

# Create your views here.
def index(request):
    #Grab crypto price data
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,ETH,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD")
    price = json.loads(price_request.content)
    #grab crypto news
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    context = {
        'api': api,
        'price': price,
        }
    return render(request, 'index.html', context)
