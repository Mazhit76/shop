from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
    path('add/<int:id>/', basketapp.basket_add, name='basket_add'),
    # Эти два URL необходимы для работы с AJAX  запросом
    path('remove/<int:id>)/', basketapp.basket_remove, name='basket_remove'),
    path('edit/<int:id>/<int:quantity>/',
         basketapp.basket_edit, name='basket_edit'),
]
# Подгружаем файлы изображений, т.е. указываем путь откуда подгружать
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
