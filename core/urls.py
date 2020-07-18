from core.views import ListPlaces
from django.urls import path

urlpatterns = [
    path('place/', ListPlaces.as_view()),
]
