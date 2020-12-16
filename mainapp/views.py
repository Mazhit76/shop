from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import ProductCategory, Product


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


def products(request, pk=None):  # pk-это то что выделено в shop/urls.py include()
    title = 'Главная'
    products = Product.objects.all()
    print(pk)  # Это мы выводим на экран терминала номер страницы которую набрали  передано в mainapp/urls.py
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
    return render(request, 'mainapp/products.html', context=content)


def test_context(request):
    content = {
        'title': 'Добро пожаловать',
        'user_name': "Иваев Мажит",
        'products': [
            {'name': 'Черное худи', 'price': '2999'},
            {'name': 'Джинсы', 'price': '4999'},
        ],
        'promotion': True,
        'promotin_produced': [
            {'name': 'Кроссовки', 'price': '1999'},
            {'name': 'Майка', 'price': '299'},
        ],
    }
    return render(request, 'mainapp/context.html', context=content)
