from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import Account
# Register your models here.


class AccountAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_admin')
    search_fields = ('email', 'username')
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)

