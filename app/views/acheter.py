
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages

from app.models import Acheter, Category, Product
from app.forms import AcheterForm

def index(request):
    assert isinstance(request, HttpRequest)
    acheter = Acheter.objects.all()
    return render(
        request,
        'app/acheter/index.html',
        {
            'acheter': acheter
        }
    )

def add(request):
    assert isinstance(request, HttpRequest)
    categories = Category.objects.all()
    form = AcheterForm()
    return render(
        request,
        'app/acheter/add.html',
        {
            'form': form,
            'categories': categories
        }
    )
    
def getProducts(request):
    category_id = request.GET.get('category_id')
    products = Product.objects.filter(category_id = category_id).order_by('product_name')
    return render(
        request,
        'app/acheter/getProducts.html',
        {
            'products': products
        }
    )
    
def getUnitPrice(request):
    id_product = request.GET.get('id_product')
    product = Product.objects.get(pk=id_product)
    return render(
        request,
        'app/acheter/getUnitPrice.html',
        {
            'product': product
        }
    )

def update(request, id):
    if request.method == 'POST':
        if id == 0:
            form = AcheterForm(request.POST)
        else:
            acheter = Acheter.objects.get(pk=id)
            form = AcheterForm(request.POST, instance=acheter)
        if form.is_valid():
            form.save()
        messages.success(request, "Achat has been updated successfully !")
        return redirect('/acheter')


def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "post":
        if id == 0:
            form = AcheterForm()
        else:
            if id == 0:
                form = AcheterForm(request.POST)
            else:
                acheter = Acheter.objects.get(pk=id)
                form = AcheterForm(request.POST, instance=acheter)
            if form.is_valid():
                form.save()
                messages.success(request, "prevision has been updated successfully !")
            return redirect('/acheter')
    else:
        acheter = Acheter.objects.get(pk=id)
        form = AcheterForm(instance=acheter)
        return render(
            request,
            'app/acheter/edit.html',
            {
                'form': form
            }
        )
def delete(request, id):
    acheter = Acheter.objects.get(pk=id)
    acheter.delete()
    messages.success(request, "Achat has been removed successfully !")
    return redirect('/acheter')

def store(request):
    if request.method == 'POST':
        form = AcheterForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, "Achat has been saved successfully !")
        return redirect('/acheter')