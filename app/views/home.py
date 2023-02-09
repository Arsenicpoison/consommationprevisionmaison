from django.http import HttpRequest
from django.shortcuts import render
from app.models import Prevision,Acheter
def index(request):
    if request.method == 'POST':
        end_date = request.POST.get('end_date')
        start_date = request.POST.get('start_date')
        
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
            difference = 0
            for prevision in previsions:
                total += prevision.total_price
            
            for acheter in acheters:
                totale +=acheter.total_price
            
            difference = total - totale
            return render(
                request,
                'app/home/index.html',
                {
                    'previsions': previsions,
                    'total': total,
                    'acheters': acheters,
                    'totale': totale,
                    'difference': difference,
                    'end_date ': end_date,
                    'start_date': start_date,
                    

                    
                }
            )
    return render(
        request,
        'app/home/index.html',
    )
    
