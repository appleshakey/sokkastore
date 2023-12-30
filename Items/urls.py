from django.urls import path
from .views import ItemHandling, CategoryHandling

urlpatterns = [
    path('', ItemHandling.as_view()),
    path('<str:category>', CategoryHandling.as_view()) 
]