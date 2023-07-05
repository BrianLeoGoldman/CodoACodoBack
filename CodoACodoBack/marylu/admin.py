from django.contrib import admin
from marylu.models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display=("username", "email",)
    list_filter=("username",)

admin.site.register(Usuario, UsuarioAdmin)
