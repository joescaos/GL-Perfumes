from django.shortcuts import render

from .models import Perfume

def home(request):

    perfumes_lista = Perfume.objects.all()

    return render(request, 'home.html', {
        'perfumes_lista': perfumes_lista,
    })