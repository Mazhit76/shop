from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from mainapp.models import ProductCategory, Product


def main(request):
    title = 'Главная'
    products = Product.objects.all()

    content = {
        'slides': [
            {'path_photo': 'vendor/img/slides/slide-1.jpg',
                'alt_text': 'First slide'},
            {'path_photo': 'vendor/img/slides/slide-2.jpg',
                'alt_text': 'Second slide'},
            {'path_photo': 'vendor/img/slides/slide-3.jpg',
                'alt_text': 'Third slide'},
        ],
        'title': title,
        'products': products,
    }
    return render(request, 'mainapp/index.html', content)


def products(request, id=None):  # pk-это то что выделено в shop/urls.py include()
    # title = 'Главная'
    # products = Product.objects.all()
    print(id)  # Это мы выводим на экран терминала номер страницы которую набрали  передано в mainapp/urls.py
    content = {
        'title': 'GeekShop - Категории',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
    }
    return render(request, 'mainapp/products.html', content)


def __str__(self):
    return self.username
