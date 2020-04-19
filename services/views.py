from django.views import generic
from .models import Service

class ServiceList(generic.ListView):
    template_name = 'services/service.html'
    context_object_name = 'services'
    model = Service
    ordering = ['-created_on']

class ServiceDetail(generic.DetailView):
    model = Service
    template_name = 'services/service_detail.html'