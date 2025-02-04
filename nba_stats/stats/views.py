import requests
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    url = "https://www.balldontlie.io/api/v1/players?per_page=10"
    response = requests.get(url)
    try:
        players = response.json().get('data', [])
    except ValueError:
        return HttpResponse(f"Error decoding JSON: {response.text}")
    return render(request, 'stats/index.html', {'players': players})
