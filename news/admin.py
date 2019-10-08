from django.contrib import admin
from .models import Article,tag

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)


admin.site.register(Article,ArticleAdmin)
admin.site.register(tag)

