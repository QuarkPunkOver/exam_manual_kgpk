from django.db import models

class User(models.Model):
    IDUser = models.AutoField(primary_key=True)
    LastName = models.CharField(max_length=255)
    FirstName = models.CharField(max_length=255)
    Patronymic = models.CharField(max_length=255, blank=True, null=True)
    Login = models.CharField(max_length=255, unique=True)
    Password = models.CharField(max_length=255)
    Gender = models.CharField(max_length=1)  #для о
    BirthDay = models.DateField()
    PhoneNumber = models.CharField(max_length=15)
    NumberPassport = models.CharField(max_length=20)
    SerialPassport = models.CharField(max_length=20)
    Block = models.BooleanField(default=False)
    FirstAuth = models.DateTimeField()
    Role = models.CharField(max_length=50)
    Addres = models.TextField()

    class Meta:
        db_table = 'User'  # имя таблицы в БД
        managed = False  # чтобы Django не думал создавать или изменять таблицу