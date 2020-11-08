from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customers/', views.customers, name='customers'),
    path('analytics/', views.analytics, name='analytics'),
    path('trends/', views.trends, name='trends')
]
