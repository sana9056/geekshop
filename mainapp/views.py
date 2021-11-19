from django.shortcuts import render


def products(request):
    return render(request, 'mainapp/products.html')
    

def contact(request):
    return render(request, 'mainapp/contact.html')


def main(request):
    context = {
        'title': 'GeekShop',
        'header': 'Добро пожаловать на сайт',
    }
    return render(request, 'mainapp/index.html', context)

