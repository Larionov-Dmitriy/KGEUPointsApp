from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from PointsApp import settings


class StudentManager(BaseUserManager):
    def create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError(_('Поле эл.почты не может быть пустым'))
        if not username:
            raise ValueError(_('Поле имени пользователя не может быть пустым'))
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, username, password, **extra_fields)

class Student(AbstractUser):
    email = models.EmailField(_('Адрес электронной почты'), unique=True)
    username = models.CharField(_('Имя пользователя'), max_length=50, unique=True)
    first_name = models.CharField(_('Имя'), max_length=50)
    second_name = models.CharField(_('Фамилия'), max_length=50)
    third_name = models.CharField(_('Отчество'), max_length=50)
    group = models.CharField(_('Группа'), max_length=10)
    institute = models.CharField(_('Институт'), max_length=20)
    hostel = models.CharField(_('Общежитие №'), max_length=1)
    photo = models.ImageField(upload_to='photos', null=True, blank=True, verbose_name='Фото пользователя')
    points = models.IntegerField(_('Баллы'), null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = StudentManager()

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return self.second_name + ' ' + self.first_name + ' ' + self.third_name


class StudentDetailPoints(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    received_points = models.IntegerField(_('Полученные балы'))
    points_activity = models.TextField(_('За что полученны баллы'))
    date = models.DateField(_('Дата полученных баллов'))

    class Meta:
        verbose_name = 'Баллы студента'
        verbose_name_plural = 'Баллы студентов'

    def __str__(self):
        return self.student.username
