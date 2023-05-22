from django.contrib import admin
from . import models

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'slug', 'author', 'published_date', 'status',
    )
    list_filter =(
        'status', 'created', 'published_date', 'author'
    )
    search_fields = ('title','body')
    prepopulated_fields = {
        'slug': ('title',)
    }
    raw_id_fields = ('author',)
    date_hierarchy = 'published_date'
    ordering = (
        'status', 'published_date'
        )