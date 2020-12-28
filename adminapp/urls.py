from django.urls import path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    #     path('', adminapp.index, name='index'),
    #     path('users/', adminapp.admin_users, name='admin_users'),
    #     path('users/create/', adminapp.admin_users_create, name='admin_users_create'),
    #     path('users/update/<int:user_id>/',
    #          adminapp.admin_users_update, name='admin_users_update'),
    #     path('users/remove/<int:user_id>/',
    #          adminapp.admin_users_remove, name='admin_users_remove'),

    path('', adminapp.index, name='index'),
    path('users/', adminapp.UsersListView.as_view(), name='admin_users'),
    path('users/create/', adminapp.UsersCreateView.as_view(),
         name='admin_users_create'),
    path('users/update/<int:pk>/', adminapp.UsersUpdateView.as_view(),
         name='admin_users_update'),
    path('users/remove/<int:pk>/', adminapp.UserDeleteView.as_view(),
         name='admin_users_remove'),

    path('admin_products_categories/', adminapp.admin_products_categories,
         name='admin_products_categories'),

    path('admin_products_categories/create/', adminapp.admin_products_categories_create,
         name='admin_products_categories_create'),

    path('admin_products_categories/update/<int:ProductCategory_id>/', adminapp.admin_products_categories_update,
         name='admin_products_categories_update'),

    path('admin_products_categories/remove/<int:ProductCategory_id>/', adminapp.admin_products_categories_remove,
         name='admin_products_categories_remove'),
]
