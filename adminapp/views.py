# Create your views here.
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm
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


# @user_passes_test(lambda u: u.is_superuser)
# def index(request):
#     return render(request, 'adminapp/index.html')


# # Следующие контроллеры демонстрируют принцип CRUD
# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_create(request):
#     # C - Create
#     if request.method == 'POST':
#         form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:admin_users'))
#             # Здесь по другому написано было
#         else:
#             print(form.errors)
#     else:
#         form = UserAdminRegisterForm()
#     context = {'form': form}
#     return render(request, 'adminapp/admin-users-create.html', context)


# @user_passes_test(lambda u: u.is_superuser)
# def admin_users(request):
#     # R - Read
#     context = {
#         'users': User.objects.all(),
#     }
#     return render(request, 'adminapp/admin-users-read.html', context)


# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_update(request, user_id):
#     # U - Update
#     user = User.objects.get(id=user_id)
#     if request.method == 'POST':
#         form = UserAdminProfileForm(
#             data=request.POST, files=request.FILES, instance=user)  # instance Экземпляр формы модели, прикрепленный к объекту модели
#         # атрибут, который дает его методам доступ к этому конкретному экземпляру модели.
#         # Здесь передают  полям текущей формы данные из объекта User
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admin_staff:admin_users'))
#     else:
#         form = UserAdminProfileForm(instance=user)

#     context = {'form': form, 'user': user}
#     return render(request, 'adminapp/admin-users-update-delete.html', context)


# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_remove(request, user_id):
#     user = User.objects.get(id=user_id)
#     # user.delete()
#     user.is_active = False
#     user.save()
#     return HttpResponseRedirect(reverse('admin_staff:admin_users'))


@user_passes_test(lambda u: u.is_superuser)
def admin_products_categories(request):
    # R - Read
    context = {
        # Внес изменения на свой класс не сработало, надо разбтраться
        'ProductsCategories': ProductCategory.objects.all(),
    }
    return render(request, 'adminapp/admin-products-categories.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_categories_create(request):
    # C - Create
    if request.method == 'POST':
        form = UserAdminProductCategory(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_products_categories'))
            # Здесь по другому написано было
        else:
            print(form.errors)
    else:
        form = UserAdminProductCategory()
    context = {'form': form}
    return render(request, 'adminapp/admin-products-category-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_categories_update(request,  ProductCategory_id):
    # U - Update
    category = ProductCategory.objects.get(id=ProductCategory_id)
    if request.method == 'POST':
        form = UserAdminCategoriesForm(
            data=request.POST, files=request.FILES, instance=category)
        # атрибут, который дает его методам доступ к этому конкретному экземпляру модели.
        # Здесь передают  полям текущей формы данные из объекта ProductCategory

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_products_categories'))
    else:
        form = UserAdminCategoriesForm(instance=category)

    context = {
        'form': form,
        'ProductCategory': category
    }
    return render(request, 'adminapp/admin-products-categories-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_categories_remove(request,  ProductCategory_id):
    # U - Update
    category = ProductCategory.objects.get(id=ProductCategory_id)
    # category.delete()
    category.is_active = False
    category.save()
    return HttpResponseRedirect(reverse('admin_staff:admin_products_categories'))


# Это было учебные методы для понятия процесса формирования url, views, models откуа вссе берется
# Ниже предаствалено современные способы обработки через классы ивстренные бииблиотеки


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'adminapp/index.html')


class UsersListView(ListView):
    model = User
    template_name = 'adminapp/admin-users-read.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class UsersCreateView(CreateView):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    success_url = reverse_lazy('adminapp:admin_users')  # Здесь по своему
    form_class = UserAdminRegisterForm


class UsersUpdateView(UpdateView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users')
    form_class = UserAdminProfileForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'GeekShop - Редактирование пользователя'
        return context


class UserDeleteView(DeleteView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
