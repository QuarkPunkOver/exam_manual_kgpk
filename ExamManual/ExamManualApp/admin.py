from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # Поля для отображения в списке объектов
    list_display = (
        'IDUser', 
        'Login', 
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
                'Patronymic',
                'Gender',
                'BirthDay',
                'PhoneNumber',
                'Addres',
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
