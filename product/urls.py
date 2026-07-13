from django.urls import path
from product.views import product_view,landing_page,game_choice,facebook,hangman

urlpatterns = [
    path('data/',product_view),
    path('landing/',landing_page),
    path('game/',game_choice),
    path('facebook/',facebook),
    path('hangman/',hangman),
]