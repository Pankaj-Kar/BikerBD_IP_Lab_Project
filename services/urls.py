from . import views
from .views import ServiceDetail, ServiceList
from django.urls import path

urlpatterns = [
    path('', ServiceList.as_view(), name='service'),
    path('<int:pk>/', ServiceDetail.as_view(), name='service-detail'),
]