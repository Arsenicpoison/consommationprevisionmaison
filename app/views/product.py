from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages

from app.models import Product,Category
from app.forms import ProductForm

def index(request):
    assert isinstance(request, HttpRequest)
    product = Product.objects.all()
    return render(
        request,
        'app/products/index.html',
        {
            'products': product
        }
    )
    
def add(request):
    form = ProductForm()
    return render(
        request, 
        'app/products/add.html',
        {
            'form': form
        }
    )

def add(request):
    assert isinstance(request, HttpRequest)
    categories = Category.objects.all()
    form = ProductForm()
    return render(
        request,
        'app/products/add.html',
        {
            'form': form,
            'categories':categories
        }
    )

    
def store(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, "product has been saved successfully !")
        return redirect('/products')
    
def update(request, id):
    if request.method == 'POST':
        if id == 0:
            form = ProductForm(request.POST)
        else:
            products = Product.objects.get(pk=id)
            form = ProductForm(request.POST, instance=products)
        if form.is_valid():
            form.save()
        messages.success(request, "provisions has been updated successfully !")
        return redirect('/products')


def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "POST":
        if id == 0:
            form = ProductForm()
        else:
            if id == 0:
                form = ProductForm(request.POST)
            else:
                products = Product.objects.get(pk=id)
                form = ProductForm(request.POST, instance=products)
            if form.is_valid():
                form.save()
                messages.success(request, "product has been updated successfully !")
            return redirect('/products')
    else:
        products = Product.objects.get(pk=id)
        form = ProductForm(instance=products)
        return render(
            request,
            'app/products/edit.html',
            {
                'form': form
            }
        )
def delete(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    messages.success(request, "Category has been removed successfully !")
    return redirect('/products')