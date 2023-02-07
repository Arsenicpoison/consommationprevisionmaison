"""consommationmaison URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from app.views import home,categories,product,previsions

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',home.index,name='home'),

    path('categories/', categories.index, name='categories_index'),
    path('categories/add', categories.add, name='categories_add'),
    path('categories/store', categories.store, name='categories_store'),
    path('categories/edit/<int:id>', categories.edit, name='categories_edit'),
    path('categories/delete/<int:id>', categories.delete, name='categories_delete'),

    path('products/', product.index, name='products_index'),
    path('products/add', product.add, name='products_add'),
    path('products/store', product.store, name='products_store'),
    path('products/update/<int:id>', product.update, name="products_update"),
    path('products/edit/<int:id>', product.edit, name='products_edit'),
    path('products/delete/<int:id>', product.delete, name='products_delete'),

    path('previsions/', previsions.index, name='previsions_index'),
    path('previsions/add', previsions.add, name='previsions_add'),
    path('previsions/store', previsions.store, name='previsions_store'),
    path('previsions/update/<int:id>', previsions.update, name="previsions_update"),
    path('previsions/edit/<int:id>', previsions.edit, name='previsions_edit'),
    path('previsions/delete/<int:id>', previsions.delete, name='previsions_delete'),


]
