from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("<h1>Bonjour bienvneu sur mon site</h1>")
    return render(request, "vercel_app/index.html", context={"date" : datetime.today()}) 
