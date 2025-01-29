from django.contrib import admin
from .models import User, Role, Gender

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # Поля для отображения в списке объектов
    list_display = (
        'IDUser', 
        'Login', 
        'FirstName',
        'SurName',
        'Patronymic', 
        'Gender', 
        'BirthDay', 
        'PhoneNumber', 
        'Role', 
        'Block', 
        'is_active'
    )

    # Поля, по которым можно фильтровать в админке
    list_filter = ('Gender', 'Role', 'Block', 'is_active')

    # Поля, по которым можно искать
    search_fields = ('Login', 'PhoneNumber', 'NumberPassport', 'SerialPassport')

    # Поля для редактирования на странице объекта
    fieldsets = (
        ('Основная информация', {
            'fields': (
                'Login',
                'FirstName',
                'SurName',
                'Patronymic',
                'Gender',
                'BirthDay',
                'PhoneNumber',
                'Addres',
                'password'
            )
        }),
        ('Документы', {
            'fields': (
                'NumberPassport',
                'SerialPassport',
            )
        }),
        ('Статус и доступ', {
            'fields': (
                'Block',
                'FirstAuth',
                'Role',
                'is_staff',
                'is_active',
                'is_superuser',
            )
        }),
    )