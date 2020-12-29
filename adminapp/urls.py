from django.urls import path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [

    path('', adminapp.index, name='index'),
    path('users/', adminapp.UsersListView.as_view(), name='admin_users'),
    path('users/create/', adminapp.UsersCreateView.as_view(),
         name='admin_users_create'),
    path('users/update/<int:pk>/', adminapp.UserUpdateView.as_view(),
         name='admin_users_update'),
    path('users/remove/<int:pk>/', adminapp.UserDeleteView.as_view(),
         name='admin_users_remove'),

    path('admin_products_categories/', adminapp.ProductCategoriesView.as_view(),
         name='admin_products_categories'),

    path('admin_products_categories/create/', adminapp.ProductCategoriesCreateView.as_view(),
         name='admin_products_categories_create'),

    path('admin_products_categories/update/<int:pk>/',
         adminapp.ProductCategoryUpdateView.as_view(),  name='admin_products_categories_update'),

    path('admin_products_categories/remove/<int:pk>/', adminapp.ProductCategoryDelete.as_view(),
         name='admin_products_categories_remove')
]
