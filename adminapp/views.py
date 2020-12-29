# Create your views here.

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from mainapp.models import ProductCategory
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test

from authapp.models import User
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, UserAdminProductCategory,  UserAdminCategoriesForm

from django.shortcuts import get_object_or_404


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'adminapp/index.html')


class UsersListView(ListView):
    # Обязательно прописать путь к этомму классу в URLS+ .as_view()
    model = User
    template_name = 'adminapp/admin-users-read.html'
    #  Но здесь будет универсальный объект на выходе который передается ключ в request
    #  имя этого ключа: object_list=====> в HTML  документах при использовании данного класса
    #  Использовать ссылку на object_list

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    # Пользователь не будет иметь доступ к странице если он не суперюзер
    def dispatch(self, request, *args, **kwargs):
        # Метод диспатч встроенный овечает за отображение страницы с пользователями
        #  мы его вызвали только для того чтобы покрыть его декоратором
        # Мы его не переоперделяем и ничего с ним не делаем
        return super(UsersListView, self).dispatch(request, *args, **kwargs)


class UsersCreateView(CreateView):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    success_url = reverse_lazy('adminapp:admin_users')  # Здесь по своему
    form_class = UserAdminRegisterForm


class UserUpdateView(UpdateView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('adminapp:admin_users')  # Здесь по своему
    form_class = UserAdminProfileForm

    def get_context_data(self, **kwargs):
        # при переопеределении не забывать передавать параметры
        #  того что мы переопределяем
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Редактирование пользователя'
        # здесь можно context.update() использоавать - это словарь
        return context


class UserDeleteView(DeleteView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('adminapp:admin_users')
# Вставили форму отправки данных
# из за того что встроенный метод удаления, который нам показали, в джанго
# не работает с кнопками.

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
# Здесь мы переопределили delete() встроенный, потомучто мы не удаляем а делаем неактивным


class ProductCategoriesView(ListView):
    model = ProductCategory
    template_name = 'adminapp/admin-products-categories.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    # Здесь необходимо использовать именно метод обертки обертки(С ума сойти!!!!!! Но работает ...)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ProductCategoriesCreateView(CreateView):
    model = ProductCategory
    template_name = 'adminapp/admin-products-category-create.html'
    success_url = reverse_lazy('adminapp:admin_products_categories')
    form_class = UserAdminProductCategory


class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/admin-products-categories-update-delete.html'
    success_url = reverse_lazy('adminapp:admin_products_categories')

    form_class = UserAdminCategoriesForm

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryUpdateView,
                        self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Редактирование категории'
        return context


#         # при переопеределении не забывать передавать параметры-name class
#         #  того что мы переопределяем
#         # здесь можно context.update() использоавать - это словарь


#         # атрибут, который дает его методам доступ к этому конкретному экземпляру модели.
#         # Здесь передают  полям текущей формы данные из объекта ProductCategory

#  Здесь я Product  в 2 местах поменял на object заработало. Потому что в
# Основное отличие класса UpdateView от CreateView, это передача экземпляра изменяемого объекта атрибуту object данного класса.


class ProductCategoryDelete(DeleteView):
    model = ProductCategory
    template_name = 'adminapp/admin-products-categories-update-delete.html'
    success_url = reverse_lazy('adminapp:admin_products_categories')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

# @user_passes_test(lambda u: u.is_superuser)
# def admin_products_categories_remove(request,  ProductCategory_id):
#     # U - Update
#     category = ProductCategory.objects.get(id=ProductCategory_id)
#     # category.delete()
#     category.is_active = False
#     category.save()
#     return HttpResponseRedirect(reverse('adminapp:admin_products_categories'))


# Это было учебные методы для понятия процесса формирования url, views, models откуа вссе берется
# Ниже предаствалено современные способы обработки через классы ивстренные бииблиотеки
