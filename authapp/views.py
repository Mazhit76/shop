from django.contrib.auth.forms import UsernameField
from django.http.response import HttpResponseRedirect
from authapp.forms import UserLoginForm, UserRegisterForm
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse

# Create your views here.


def login(request):
    # форму заполняем данными полученными с сайта POST
    form = UserLoginForm(data=request.POST)  # Объявили форму и метод
    if request.method == 'POST' and form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        # Здесь мы проверяем и проводим авторизацию, если все правильно то
        # Отправляем на главную страницу
        user = auth.authenticate(username=username, password=password)
        # этот метод берет данные из б.д. пользователей и проверяет на
        # совпадение и на его активность
        if user and user.is_active:
            auth.login(request, user)  # Производлим авторизацию
            # отправляем главную страницу
            return HttpResponseRedirect(reverse('main'))
    context = {'form': form}  # Форму передали в контекст
    return render(request, 'authapp/login.html', context)


def profile(request):
    return render(request, 'authapp/profile.html')


def register(request):
    # Выдавал ошибку проверку взял с файла уроку 4
    if request.method == 'POST':
        # Создаем новую форму и передаем ей данные из запроса
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():  # Здесь мы проверяем методам джанго правильность ввода логина и имени
            form.save()
            # Если все ок то сохраняем форму
            messages.success(request, 'Вы успешно зарегистрировались!')
            new_user = auth.authenticate(
                username=form.cleaned_data['username'], password=form.cleaned_data['password2'])
            auth.login(request, new_user)
            # Если все правильно то авторизуем и отправляем на страницу товаров
            return HttpResponseRedirect(reverse('mainapp:index'))
# Если неправильно то заново создаем метод создания формы
    else:
        form = UserRegisterForm()

    context = {'form': form}  # Форму передали в контекст

    return render(request, 'authapp/register.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))
