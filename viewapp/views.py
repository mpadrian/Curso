from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def holamundo(request):
    return render(request, 'main.html')

class adios_mundo(TemplateView):
    template_name = 'adios.html'
    def get(self, request):
        return render(request, 'adios.html')

