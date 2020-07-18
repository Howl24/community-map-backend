from rest_framework import status

from core.models import Place, Category
from core.serializers import PlaceSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class ListCreateCategories(APIView):

    def get(self, request):
        categories = Category.scan()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListPlaces(APIView):

    def get(self, request):
        places = Place.scan()
        serializer = PlaceSerializer(places, many=True)
        return Response(serializer.data)


class BatchCreatePlaces(APIView):

    def post(self, request):
        serializer = PlaceSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
