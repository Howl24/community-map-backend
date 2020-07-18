from core.views import ListPlaces, ListCreateCategories, BatchCreatePlaces
from django.urls import path

urlpatterns = [
    path('category/', ListCreateCategories.as_view()),
    path('place/', ListPlaces.as_view()),
    path('place/batch', BatchCreatePlaces.as_view()),
]
