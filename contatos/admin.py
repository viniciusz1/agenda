from django.contrib import admin

# Register your models here.
from .models import Categoria, Contato

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id','nome','sobrenome','telefone','email','data_criacao','categoria')
    list_display_links = ('id','nome','sobrenome')
    list_filter = ('nome','sobrenome')
    list_per_page = 10
admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)