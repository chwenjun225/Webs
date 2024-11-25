from django.shortcuts import render

from .models import Musician

def musicians(request):
    data = {
        'musicians': Musician.objects.all().order_by('last_name'), 
    }
    return render(request, "musicians.html", data)
