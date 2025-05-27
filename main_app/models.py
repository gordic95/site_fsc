from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, first_name, last_name, password, **extra_fields):
        """
        Создание и сохранение пользователя с указанной почтой и паролем.
        """
        if not email:
            raise ValueError(_("Email must be provided"))
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, first_name, last_name, password, **extra_fields)

    def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self._create_user(email, first_name, last_name, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name=_('Электронная почта'), max_length=255, unique=True)
    first_name = models.CharField(verbose_name=_('Имя'), max_length=150)
    last_name = models.CharField(verbose_name=_('Фамилия'), max_length=150)
    birth_day = models.DateField(verbose_name=_('дата рождения'), null=True, blank=True)
    gender = models.CharField(verbose_name=_('Пол'), max_length=15, choices=[('Мужчина', _('Мужчина')), ('Женищна', _('Женщина'))], blank=True)
    bio = models.TextField(verbose_name=_('О себе'), blank=True)
    location = models.CharField(verbose_name=_('Город'), max_length=100, blank=True)
    avatar = models.ImageField(default='default/default_photo.png', verbose_name=_('Фото профиля'), upload_to='avatars/', null=True, blank=True)
    is_staff = models.BooleanField(verbose_name=_('Доступ к админ-панели'), default=False)
    is_superuser = models.BooleanField(verbose_name=_('Администратор'), default=False)
    is_active = models.BooleanField(verbose_name=_('Активен'), default=True)
    rating = models.PositiveIntegerField(verbose_name=_('Рейтинг'), default=0)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)


    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')
        ordering = ['email']

