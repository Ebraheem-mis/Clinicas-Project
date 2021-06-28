from django.shortcuts import render
from .models import Service
# Create your views here.



def services_list_view(request):
  data={}
  service_list = Service.objects.all()
  data['Service'] = service_list
  return render(request, "service_list_view.html", context=data)