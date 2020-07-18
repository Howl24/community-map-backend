from core.views import ListPlaces, ListCreateCategories
from django.urls import path

urlpatterns = [
    path('category/', ListCreateCategories.as_view()),
    path('place/', ListPlaces.as_view()),
]
