from django.shortcuts import render


def products(request):
    context = {
        'products': [
            {
                "name": "Стул повышенного качества",
                "price": "123",
                "description": "Не оторваться.",
                "image": "img/product-11.jpg"
            },
            {
                "name": "Стул №1",
                "price": "",
                "description": "Ещё один стул",
                "image": "img/product-21.jpg"
            },
            {
                "name": "Памперсы",
                "price": "",
                "description": "Какой-то товар лишь бы был",
                "image": "img/product-31.jpg"
            },
            {
                "name": "Что-то 3",
                "price": "",
                "description": "А вот это уже было кстати",
                "image": "img/product-11.jpg"

            },
            {
                "name": "Стул 2",
                "price": "",
                "description": "А это вообще не стул",
                "image": "img/product-51.jpg"
            },
            {
                "name": "Стул 777",
                "price": "",
                "description": "Кажется тоже не стул",
                "image": "img/product-61.jpg"
            },
        ]
    }
    return render(request, 'mainapp/products.html', context)
    

def contact(request):
    return render(request, 'mainapp/contact.html')


def main(request):
    context = {
        'title': 'GeekShop',
        'header': 'Добро пожаловать на сайт',
    }
    return render(request, 'mainapp/index.html', context)

