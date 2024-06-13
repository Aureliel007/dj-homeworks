from django.urls import path

from .views import SensorAPIListView, SensorAPIDetailView, MeasurementAPIView

urlpatterns = [
    path('sensors/', SensorAPIListView.as_view()),
    path('sensors/<pk>/', SensorAPIDetailView.as_view()),
    path('measurements/', MeasurementAPIView.as_view()),
]
