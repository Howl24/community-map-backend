from rest_framework import serializers

from core.models import Place, Category


class CategorySerializer(serializers.Serializer):
    id = serializers.CharField(source='uuid')
    description = serializers.CharField()
    icon = serializers.CharField()

    def create(self, validated_data):
        category = Category(
            validated_data.get('uuid'),
            description=validated_data.get('description'),
            icon=validated_data.get('icon'),
        )
        category.save()
        return category


class PlaceSerializer(serializers.Serializer):
    id = serializers.CharField(source='uuid')
    description = serializers.CharField()
    latitude = serializers.CharField()
    longitude = serializers.CharField()
    category = serializers.CharField()

    def create(self, validated_data):
        place = Place(
            validated_data.get('uuid'),
            description=validated_data.get('description'),
            latitude=validated_data.get('latitude'),
            longitude=validated_data.get('longitude'),
            category=validated_data.get('category'),
        )
        place.save()
        return place
