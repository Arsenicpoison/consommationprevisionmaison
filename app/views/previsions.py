from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages

from app.models import Prevision, Category, Product
from app.forms import PrevisionForm

def index(request):
    assert isinstance(request, HttpRequest)
    previsions = Prevision.objects.all()

    return render(
        request,
        'app/previsions/index.html',
        {
            'previsions': previsions
        }
    )

def add(request):
    assert isinstance(request, HttpRequest)
    categories = Category.objects.all()
    products = Product.objects.all()
    form = PrevisionForm()
    return render(
        request,
        'app/previsions/add.html',
        {
            'form': form,
            'categories': categories,
            'products':products
        }
    )
    
def getProducts(request):
    category_id = request.GET.get('category_id')
    products = Product.objects.filter(category_id = category_id).order_by('product_name')
    return render(
        request,
        'app/previsions/getProducts.html',
        {
            'products': products
        }
    )
    
def getUnitPrice(request):
    id_product = request.GET.get('id_product')
    product = Product.objects.get(pk=id_product)
    return render(
        request,
        'app/previsions/getUnitPrice.html',
        {
            'product': product
        }
    )

def update(request, id):
    if request.method == 'POST':
        if id == 0:
            form = PrevisionForm(request.POST)
        else:
            previsions = Prevision.objects.get(pk=id)
            form = PrevisionForm(request.POST, instance=previsions)
        if form.is_valid():
            form.save()
        messages.success(request, "provisions has been updated successfully !")
        return redirect('/previsions')


def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "post":
        if id == 0:
            form = PrevisionForm()
        else:
            if id == 0:
                form = PrevisionForm(request.POST)
            else:
                prevision = Prevision.objects.get(pk=id)
                form = PrevisionForm(request.POST, instance=prevision)
            if form.is_valid():
                form.save()
                messages.success(request, "prevision has been updated successfully !")
            return redirect('/previsions')
    else:
        prevision = Prevision.objects.get(pk=id)
        form = PrevisionForm(instance=prevision)
        return render(
            request,
            'app/previsions/edit.html',
            {
                'form': form
            }
        )
def delete(request, id):
    prevision = Prevision.objects.get(pk=id)
    prevision.delete()
    messages.success(request, "prevision has been removed successfully !")
    return redirect('/previsions')

def store(request):
    if request.method == 'POST':
        form = PrevisionForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, "prevision has been saved successfully !")
        return redirect('/previsions')
    
def result(request):
    if request.method == 'POST':
        date_from =request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        searchbar = Prevision.objects.raw('select category,product_name,update_price,quantity,total_price where date between " '+date_from+' " and " '+date_to+' "')
