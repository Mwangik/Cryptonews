import requests
import json

from django.shortcuts import render

# Create your views here.
def index(request):
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    context = {'api': api}
    return render(request, 'index.html', context)
