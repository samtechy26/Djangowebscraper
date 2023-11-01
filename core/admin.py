from django.contrib import admin
from .models import NewsItem


class NewsItemAdmin(admin.ModelAdmin):
    list_display = [
        'source',
        'link',
        'title',
        'publish_date',
    ]


admin.site.register(NewsItem, NewsItemAdmin)
