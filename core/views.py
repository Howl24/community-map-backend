from core.models import Place
from core.serializers import PlaceSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class ListPlaces(APIView):

    def get(self, request):
        places = Place.scan()
        serializer = PlaceSerializer(places, many=True)
        return Response(serializer.data)
