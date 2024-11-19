from django.urls import path
from authentication.views import *

app_name = 'authentication'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('create-flutter/', create_product_flutter, name='create_mood_flutter'),
    path('logout/', logout, name='logout'),
]