from django.contrib import admin

from .models import Contato, Categoria

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome','sobrenome','telefone','descricao', 'categoria')

admin.site.register(Contato, ContatoAdmin)
admin.site.register(Categoria)
