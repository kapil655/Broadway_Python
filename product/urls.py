from django.urls import path
from home.views import project_delete
from product.views import product_view,landing_page,product_list,product_create,game_choice,facebook,hangman,product_update


urlpatterns = [
    path('data/',product_view),
    path('landing/',landing_page),
      path('game/',game_choice),
      path('facebook/',facebook),
      path('hangman/',hangman),
    path('product_list/',product_list),
    path('create/',product_create),
    path('update/<int:id>',product_update),
    path('delete/<int:id>',project_delete), 
]
