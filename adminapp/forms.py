from django.db import models
from django.db.models import fields
from mainapp.views import products
from django import forms

from authapp.forms import UserRegisterForm, UserProfileForm
from authapp.models import User
from mainapp.models import ProductCategory


class UserAdminRegisterForm(UserRegisterForm):
    avatar = forms.ImageField(widget=forms.FileInput())
    # Если не переопределить этот аватар то появится поле для изменения -встроеенная от джанго

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name',
                  'password1', 'password2', 'avatar')

    def __init__(self, *args, **kwargs):
        super(UserAdminRegisterForm, self).__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs['class'] = 'custom-file-input'


class UserAdminProfileForm(UserProfileForm):

    def __init__(self, *args, **kwargs):
        super(UserAdminProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = False
        self.fields['email'].widget.attrs['readonly'] = False


class UserAdminProductCategory(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ('name', 'descripthion')
        # managed = True
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __init__(self, *args, **kwargs):
        super(UserAdminProductCategory, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

        # self.fields['name'].widget.attrs['readonly'] = False
        # self.fields['descripthion '].widget.attrs['readonly'] = False


class UserAdminCategoriesForm(UserAdminProductCategory):

    def __init__(self, *args, **kwargs):
        super(UserAdminCategoriesForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['readonly'] = False
        self.fields['descripthion'].widget.attrs['readonly'] = False
