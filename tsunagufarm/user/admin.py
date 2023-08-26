from django.contrib import admin

from user.models import User

@admin.register(User)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
