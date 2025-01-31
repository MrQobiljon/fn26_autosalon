from django.urls import path

from .views import (CarAPIView, CarDetailApiView)

urlpatterns = [
    path('cars/', CarAPIView.as_view()),
    path('cars/<int:car_id>/', CarDetailApiView.as_view()),
]