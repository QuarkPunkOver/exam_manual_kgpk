from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, Login, password=None, **extra_fields):
        if not Login:
            raise ValueError("Поле Login должно быть заполнено")
        user = self.model(Login=Login, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, Login, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError("Суперпользователь должен иметь is_staff=True")
        if not extra_fields.get('is_superuser'):
            raise ValueError("Суперпользователь должен иметь is_superuser=True")

        return self.create_user(Login, password, **extra_fields)

class User(AbstractBaseUser):
    IDUser = models.AutoField(primary_key=True)
    Patronymic = models.CharField(max_length=255, blank=True, null=True, verbose_name='Отчество')
    Login = models.CharField(max_length=255, unique=True, verbose_name='Логин')
    Gender = models.CharField(max_length=1, default=5, verbose_name='Пол')
    BirthDay = models.DateField(default='2000-01-01', verbose_name='Дата рождения')
    PhoneNumber = models.CharField(max_length=15, default='none', verbose_name='Номер телефона')
    NumberPassport = models.CharField(max_length=20, verbose_name='Номер паспорта')
    SerialPassport = models.CharField(max_length=20, verbose_name='Серия паспорта')
    Block = models.BooleanField(default=False, verbose_name='Заблокирован')
    FirstAuth = models.BooleanField(default=True, verbose_name='Первичная авторизация')
    Role = models.IntegerField(default=2, verbose_name='Роль')
    Addres = models.TextField(verbose_name='Адрес')

    # Поля для управления разрешениями
    is_staff = models.BooleanField(default=False, verbose_name='Персонал')
    is_active = models.BooleanField(default=True, verbose_name='Активный акк')
    is_superuser = models.BooleanField(default=False, verbose_name='СуперПользователь')


    objects = UserManager()

    USERNAME_FIELD = 'Login'
    REQUIRED_FIELDS = []
    

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        return True
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        db_table = 'User'  # имя таблицы в БД
    
    