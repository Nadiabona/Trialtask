from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model


User=get_user_model()

admin.site.unregister(Group)  # убираем из админки закладку Группы

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass
    # add_form_template = "admin/auth/user/add_form.html"
    # change_user_password_template = None
    # CustomUserAdmin(UserAdmin) можно так PersonalAdmin(admin.ModelAdmin) но пароль в админке не поменять
    # наследование от UserAdmin, а не от admin.ModelAdmi позволяет не писать list_filter и search_fields
    #Класс настройки админпанели.


    # exclude = ('password',) # У пользователя скрыт пароль.
    # list_display = ('username', 'email', 'first_name', "last_name")
    # readonly_fields = ('last_login','date_joined')
    # 
    # fieldsets = (  # можно настраивать так по разделам и конкретным полям
    #     (None, {'fields': ('password', 'username')}),
    #     ('Персональная информация', {'fields': ('first_name', 'last_name', 'email')}),
    #     ('Разрешения', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    #     ('Важные даты', {'fields': ('last_login', 'date_joined')}),
    # )"""



