from django.urls import path
import mainapp.views as mainapp
app_name = 'mainapp'
urlpatterns = [
    # Теперь обращаемся products:index тогда попадем
    path('', mainapp.products, name='index'),
    # на страницу products иначе ошибка, так как В path('products/', include('mainapp.urls', namespace='products')),
    # в shop urls прописали
    path('<int:category_id>/', mainapp.products, name='product'),
    path('page/<int:page>/', mainapp.products,
         name='page'),  # Поменяли путь на page
    # для вставки постраничного отображениея

]
