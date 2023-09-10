from django.core.exceptions import ValidationError
from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin, AbstractBaseUser

from utils.choices import UserRoleChoices
import re

PASSPORT_REGEX = r"^[A-Za-z]{2}\d{7}$"
PHONE_NUMBER_REGEX = r"^998\d{9}$"


class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        """
        Creates and saves a User with the given username and password.
        """

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_reader(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_reader', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(username, password, **extra_fields)

    def create_staff(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(username, password, **extra_fields)


def validate_phone_number(value: str):
    if not re.match(PHONE_NUMBER_REGEX, value):
        raise ValidationError('Номер телефона должен быть в формате 998xxxxxxxxx')
    return value


class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(max_length=70, blank=True, null=True, unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='ФИО')
    phone_number = models.CharField(max_length=12,
                                    null=True, blank=True,
                                    verbose_name='Номер телефона',
                                    validators=[validate_phone_number, ])
    birthday = models.DateField(null=True, blank=True, verbose_name='День рождения')
    profile_photo = models.ImageField(upload_to='user/profile_photos', null=True, blank=True,
                                      verbose_name='Фото профиля',
                                      default='user/profile_photos/default.png')

    is_reader = models.BooleanField(default=False, verbose_name='Читатель')

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["full_name"]

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'

    objects = UserManager()


class UserRole(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='user_roles',
                             verbose_name='Foydalanuvchi')
    role = models.CharField(max_length=26,
                            choices=UserRoleChoices.choices,
                            default=UserRoleChoices.READER,
                            verbose_name='Roli')

    class Meta:
        verbose_name = 'Foydalanuvchi roli'
        verbose_name_plural = 'Foydalanuvchi rollari'
        ordering = ('-id',)

    def __str__(self):
        return f'{self.role} - {self.user}'


def validate_passport(value: str):
    if not re.match(PASSPORT_REGEX, value):
        raise ValidationError(
            f'{value} is not a valid passport number (format: AA1234567)'
        )
    return value.upper()


class UserReader(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='user_reader',
                                verbose_name='Foydalanuvchi')
    address = models.CharField(max_length=255,
                               verbose_name='Manzil',
                               null=True, blank=True)
    passport = models.CharField(max_length=9,
                                verbose_name='Pasport raqami',
                                unique=True,
                                validators=[validate_passport])
    registration = models.CharField(max_length=255,
                                    verbose_name='Место регистрации',
                                    blank=True, null=True)

    class Meta:
        verbose_name = 'O\'quvchi'
        verbose_name_plural = 'O\'quvchilar'
        ordering = ('id',)

    def __str__(self):
        return f'{self.user}'
