from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display =('slug','titulo','conteudo','autor','status','publicado_em')
    list_filter =('autor','status')
    search_fields = ('slug','titulo','conteudo')
    prepopulated_fields = {'slug':('titulo',)}
    raw_id_fields = ('autor',)
    date_hierarchy = 'publicado_em'
    ordering = ('status', 'publicado_em')