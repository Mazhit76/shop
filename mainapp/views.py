from django.shortcuts import render

# Create your views here.


def main(request):
    return render(request, 'mainapp/index.html')


def products(request):
    return render(request, 'mainapp/products.html')


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
