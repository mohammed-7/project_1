from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('',views.navbar),
    path('',views.carousel),
    path('',views.cards),
    
]
