from django.shortcuts import render


def main(request):

    content = {
        'title': 'GeekShop'
    }
    return render(request, 'mainapp/index.html', content)


def products(request):
    content = {
        'title': 'GeekShop - Категории'
    }
    return render(request, 'mainapp/products.html', content)


def test_context(request):
    """Test function for getting acquainted with the context."""
    context = {
        'title': 'Test Context',
        'header': 'Добро пожловать на сайт!',
        'username': 'Иваев Мажит',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '5 090,00 руб.'},
            {'name': 'Синяя куртка The North Face', 'price': '33 725,00 руб.'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '4 390,00 руб.'},
        ]
    }
    return render(request, 'mainapp/test_context.html', context)

    return render(request, 'mainapp/index.html')


def products(request):
    return render(request, 'mainapp/products.html')

