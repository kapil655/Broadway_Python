from django.urls import path
from home.views import project_delete
from product.views import product_view,landing_page,product_list,product_create,game_choice,facebook,hangman,product_update


urlpatterns = [
    path('data/',product_view,name="product-view"),
    path('landing/',landing_page,name="landing"),
      path('game/',game_choice,name="game"),
      path('facebook/',facebook,name="facebook"),
      path('hangman/',hangman,name="hangman"),
    path('product_list/',product_list,name="product-list"),
    path('create/',product_create,name="create"),
    path('update/<int:id>',product_update,name="product-update"),
    path('delete/<int:id>',project_delete,name="product-delete"), 
]
