from django.shortcuts import redirect,render
from django.http import HttpRequest

from app.models import Category,Prevision,Acheter

def printprevisions(request):
    assert isinstance(request, HttpRequest)
    page_title = 'Print All Previsions'
    previsions = Prevision.objects.all()
    return render(
        request,
        'app/prints/previsions.html',
        {
            'previsions' : previsions,
            'page_title' : page_title
        }
    )

def printconsommations(request):  
    assert isinstance(request, HttpRequest)
    page_title = 'Print All Consommations'
    consommations = Acheter.objects.all()
    return render(
        request,
        'app/prints/consommations.html',
        {
            'consommations': consommations,
            'page_title' : page_title
        }
    )




def resume(request):
    assert isinstance(request, HttpRequest)
    page_title = 'Print All'
    acheter = Acheter.objects.all()
    previsions = Prevision.objects.all()
    
    
    return render(
        request,
        'app/prints/resume.html',
        {
            'acheter' : acheter,
            'previsions' : previsions,
            'page_title' : page_title,
        }
    )