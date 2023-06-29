from django.urls import path
from api import views

urlpatterns = [
    path('drinks/', views.drinklist),
    path('drinks/<int:id>', views.drink_detail)
]