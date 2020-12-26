# Create your views here.
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test

from authapp.models import User
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm

from django.shortcuts import get_object_or_404
from adminapp.forms import ProductCategoryEditForm


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'adminapp/index.html')


# Следующие контроллеры демонстрируют принцип CRUD
@user_passes_test(lambda u: u.is_superuser)
def admin_users_create(request):
    # C - Create
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_users'))
            # Здесь по другому написано было
        else:
            print(form.errors)
    else:
        form = UserAdminRegisterForm()
    context = {'form': form}
    return render(request, 'adminapp/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users(request):
    # R - Read
    context = {
        'users': User.objects.all(),
    }
    return render(request, 'adminapp/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_update(request, user_id):
    # U - Update
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserAdminProfileForm(
            data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
    else:
        form = UserAdminProfileForm(instance=user)

    context = {'form': form, 'user': user}
    return render(request, 'adminapp/admin-users-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_remove(request, user_id):
    user = User.objects.get(id=user_id)
    # user.delete()
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admin_staff:admin_users'))


def admin_products_categories(request):
    title = 'админка/категории'
    categories_list = ProductCategoryEditForm.objects.all()
    context = {
        'title': title,
        'objects': categories_list
    }
    return render(request, 'adminapp/admin_products_categories.html', context)


# def category_create(request):
#     pass


# def category_update(request, pk):
#     pass


# def category_delete(request, pk):
#     pass


# def products(request, pk):
#     title = 'админка/продукт'

#     category = get_object_or_404(ProductCategory, pk=pk)
#     products_list = Product.objects.filter(category__pk=pk).order_by('name')

#     content = {
#         'title': title,
#         'category': category,
#         'objects': products_list,
#     }

#     return render(request, 'adminapp/products.html', content)


# def product_create(request, pk):
#     pass


# def product_read(request, pk):
#     pass


# def product_update(request, pk):
#     pass


# def product_delete(request, pk):
#     pass
