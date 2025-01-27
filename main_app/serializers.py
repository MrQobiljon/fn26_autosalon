from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser

from .models import Car


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    description = serializers.CharField(required=False)
    price = serializers.DecimalField(max_digits=15, decimal_places=2)
    brand_id = serializers.IntegerField()

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance: Car, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.price = validated_data.get("price", instance.price)
        instance.brand_id = validated_data.get("brand_id", instance.brand_id)
        instance.save()
        return instance






# def serialization():
#     car = Car.objects.get(pk=1)
#     serializer = CarSerializer(car)
#     print(serializer.data)
#
#     json = JSONRenderer().render(serializer.data)
#     print(json)
#
#
# def deserialization():
#     json = b'{"id":1,"name":"Tayota miniven","description":"sdfsf","price":"15.00","brand_id":3}'
#     stream = io.BytesIO(json)
#     data = JSONParser().parse(stream)
#     print(data)
#
#     serializer = CarSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
