from django.shortcuts import render

# Create your views here.


def main(request):
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
    return render(request, 'mainapp/index.html', context=content)


def products(request):
    content = {
        'slides': [
            {'path_photo': 'vendor/img/slides/slide-1.jpg',
                'alt_text': 'First slide'},
            {'path_photo': 'vendor/img/slides/slide-2.jpg',
                'alt_text': 'Second slide'},
            {'path_photo': 'vendor/img/slides/slide-3.jpg',
                'alt_text': 'Third slide'},
        ],
        'categorys': [
            {'name': 'Новинки'},
            {'name': 'Одежда'},
            {'name': 'Обувь'},
            {'name': 'Аксессуары'},
            {'name': 'Подарки'},
        ],
        'produced': [
            {'name': 'Худи черного цвета с монограммами adidas Originals',
             'descriptions': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
             'path_photo': 'vendor/img/products/Adidas%20hoodie.png',
             'price': '6 090,00'},
            {'name': 'Синяя куртка The North Face',
             'descriptions': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
             'path_photo': 'vendor/img/products/Blue%20jacket%20The%20North%20Face.png',
             'price': '23 725,00'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
             'descriptions': 'Материал с плюшевой текстурой. Удобный и мягкий.',
             'path_photo': 'vendor/img/products/Brown%20sports%20oversized-top%20ASOS%20DESIGN.png',
             'price': '3 390,00'},
            {'name': 'Черный рюкзак Nike Heritage',
             'descriptions': 'Плотная ткань. Легкий материал.',
             'path_photo': 'vendor/img/products/Black%20Nike%20Heritage%20backpack.png',
             'price': '2 340,00'},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
             'descriptions': 'Гладкий кожаный верх. Натуральный материал.',
             'path_photo': 'vendor/img/products/Black%20Dr%20Martens%20shoes.png',
             'price': '13 590,00'},
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
             'descriptions': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
             'path_photo': 'vendor/img/products/Dark%20blue%20wide-leg%20ASOs%20DESIGN%20trousers.png',
             'price': '2 890,00 руб.'},
        ],
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
