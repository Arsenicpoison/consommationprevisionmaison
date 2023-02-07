from django.http import HttpRequest
from django.shortcuts import render
from app.models import Prevision,Acheter
def index(request):
    total_prevision=Prevision.objects.count()
    total_acheter=Acheter.objects.count()
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        if start_date == "" or end_date == "":
            return render(
                request,
                'app/home/index.html',
            )
        else:
            previsions = Prevision.objects.filter(date__range=[start_date,end_date])
            acheters = Acheter.objects.filter(date__range=[start_date,end_date])
            total = 0
            totale = 0
            for prevision in previsions:
                total += prevision.total_price
            
            for acheter in acheters:
                totale +=acheter.total_price
            return render(
                request,
                'app/home/index.html',
                {
                    'previsions': previsions,
                    'total': total,
                    'acheters': acheters,
                    'totale': totale,
                    'total_prevision': total_prevision,
                    'total_acheter':total_acheter,
                    
                }
            )
    return render(
        request,
        'app/home/index.html',
    )
    
