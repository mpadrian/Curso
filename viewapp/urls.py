from django.urls import path
from viewapp.views import holamundo,adios_mundo

urlpatterns = [
    path('', holamundo),
    path('viewapp', adios_mundo.as_view()),
    #as_view() se usa para convertir una clase en una vista
]