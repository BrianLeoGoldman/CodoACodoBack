from django.contrib import admin
from marylu.models import User

class UserAdmin(admin.ModelAdmin):
    list_display=("username", "email",)
    list_filter=("username",)

admin.site.register(User, UserAdmin)
