from django.urls import path
from main import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('acao/', views.acao, name='acao'),
    path('view/',views.view, name="view")
]
