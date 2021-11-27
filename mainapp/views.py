from django.shortcuts import render
from .models import ProductCategory, Product


def products(request, pk=None):
    print(pk)
    title = 'Catalogue'
    products = Product.objects.all()[:4]

    content = {'title': title, 'products': products}
    return render(request, 'mainapp/products.html', content)
    

def contact(request):
    return render(request, 'mainapp/contact.html')


def main(request):
    title = 'GeekShop'

    products = Product.objects.all()[:4]

    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', content)

