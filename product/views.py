from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def product_view(request):
    return HttpResponse("<h1>This is product view</h1>")

def landing_page(request):
    context = {
        "name":"kapil",
        "naam":"कपिल",

    }  
    return render(request,'product/index.html',context)

def game_choice(request):
    return render(request,'product/game.html')

def facebook(request):
    return render(request,'product/facebook.html')

def hangman(request):
    return render(request, 'product/hangman.html')