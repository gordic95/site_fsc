from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.utils.translation import gettext_lazy as _
from . models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Электронная почта', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', 'birth_day', 'gender', 'bio', 'location', 'avatar')
        labels = {
            'first_name': _('Имя'),
            'last_name': _('Фамилия'),
            'birth_day': _('Дата рождения'),
            'gender': _('Пол'),
            'bio': _('О себе'),
            'location': _('Город'),
            'avatar': _('Фото профиля'),
            'password1': _('Пароль'),
            'password2': _('Повторите пароль'),
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_day': forms.DateInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

        def clean_email(self):
            email = self.cleaned_data['email']
            if get_user_model.objects.filter(email=email).exists():
                raise forms.ValidationError(_("Пользователь с таким email уже существует."))
            return email


class LoginForm(AuthenticationForm):
    # email = forms.EmailField(label='Электронная почта', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = get_user_model()
        fields = ('email', 'password')


class ProfileUpdateForm(forms.ModelForm):
    email = forms.EmailField(disabled=True, label='Электронная почта', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'birth_day', 'gender', 'bio', 'location', 'avatar')
        labels = {
            'first_name': _('Имя'),
            'last_name': _('Фамилия'),
            'birth_day': _('Дата рождения'),
            'gender': _('Пол'),
            'bio': _('О себе'),
            'location': _('Город'),
            'avatar': _('Фото профиля'),
            'email': _('Электронная почта'),
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_day': forms.DateInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class UserPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['old_password', 'new_password1', 'new_password2']
        widgets = {
            'old_password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'new_password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'new_password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'old_password': _('Старый пароль'),
            'new_password1': _('Новый пароль'),
            'new_password2': _('Повторите новый пароль'),
        }



