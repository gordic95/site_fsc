from django.contrib.auth import logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from . models import CustomUser
from .forms import CustomUserCreationForm, LoginForm, ProfileUpdateForm, UserPasswordChangeForm




class MainView(LoginRequiredMixin, ListView):
    """Функция для отображения главной страницы"""
    model = get_user_model()
    template_name = 'main.html'
    context_object_name = 'users'
    extra_context = {'title': 'Главная страница'}


class RegistrationView(CreateView):
    """Функция для регистрации пользователя"""
    form_class = CustomUserCreationForm
    template_name = 'registration/registration.html'
    extra_context = {'title': 'Регистрация пользователя'}

    def get_success_url(self):
        return reverse_lazy('main_app:login')


class LoginUserView(LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'
    extra_context = {'title': 'Авторизация пользователя'}


class LogoutView(LoginRequiredMixin, View):
    """Функция для выхода пользователя с сайта"""
    def get(self, request):
        return render(request, 'registration/logout.html')


    def post(self, request):
        logout(request)
        return redirect('main_app:login')


class ProfileView(LoginRequiredMixin, DetailView):
    """Функция для просмотра профиля пользователя"""
    model = get_user_model()
    template_name = 'profile/profile.html'
    extra_context = {'title': 'Профиль пользователя'}


    def get_object(self, *args, **kwargs):
        return self.request.user


class UserProfileDetailView(LoginRequiredMixin, DetailView):
    """Функция для просмотра профиля пользователя по его id"""
    model = get_user_model()
    template_name = 'profile/profile_detail.html'
    extra_context = {'title': 'Профиль пользователя'}
    context_object_name = 'user_profile'


class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'profile/password_change.html'
    success_url = reverse_lazy('main_app:password_change_done')
    extra_context = {'title': 'Изменение пароля пользователя'}




class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUpdateForm
    template_name = 'profile/update.html'
    extra_context = {'title': 'Редактирование профиля пользователя'}

    def get_success_url(self):
        return reverse_lazy('main_app:profile')


    def get_object(self, *args, **kwargs):
        return self.request.user


class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'profile/password_change.html'
    success_url = reverse_lazy('main_app:password_change_done')
    extra_context = {'title': 'Изменение пароля пользователя'}