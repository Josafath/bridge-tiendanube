# apps/dashboard/views.py
from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    context = {
        'total_orders': 124,
    }
    return render(request, 'dashboard/index.html', context)


def test(request):
    
    return HttpResponse("HOlaaaaaa")

# Create your views here.
