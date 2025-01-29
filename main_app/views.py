from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import generics

from django.forms import model_to_dict

from .models import Car, Brand
from .serializers import CarSerializer
from .permissions import CarPermission







# class CarListAPIView(APIView):
#     queryset = Car.objects.all()
#     permission_classes = [CarPermission]
#
#     def get(self, request: Request, pk=None):
#         if not pk:
#             cars = Car.objects.all()
#             return Response(CarSerializer(cars, many=True).data)
#         else:
#             try:
#                 car = Car.objects.get(pk=pk)
#                 return Response(CarSerializer(car).data)
#             except:
#                 return Response(status=404)
#
#     def post(self, request: Request, pk=None):
#         if pk:
#             return Response("Method POST not allowed!", status=status.HTTP_405_METHOD_NOT_ALLOWED)
#
#         serializer = CarSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         car = serializer.create(serializer.validated_data)
#
#         return Response(CarSerializer(car).data)
#
#     def put(self, request: Request, pk=None):
#         if not pk:
#             return Response("Method PUT not allowed!", status=status.HTTP_405_METHOD_NOT_ALLOWED)
#
#         try:
#             car = Car.objects.get(pk=pk)
#             serializer = CarSerializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             car = serializer.update(car, serializer.validated_data)
#             return Response(CarSerializer(car).data)
#         except Exception as e:
#             return Response(f"{e}", status=status.HTTP_404_NOT_FOUND)
#
#
#     def delete(self, request: Request, pk=None):
#         if not pk:
#             return Response("Method DELETE not allowed!", status=status.HTTP_405_METHOD_NOT_ALLOWED)
#
#         try:
#             car = Car.objects.get(pk=pk)
#             car.delete()
#         except Exception as e:
#             return Response(f"{e}", status=status.HTTP_404_NOT_FOUND)
#
#         return Response('delete my')
