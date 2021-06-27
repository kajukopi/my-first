from django.contrib import admin
from django.contrib.admin.sites import AdminSite

from .models import  Blog, Choice

class BlogInline(admin.TabularInline):
    model = Choice
    extra = 2

class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['blog_text']}),
        (None,               {'fields': ['blog_subject']}),
        ('Date information', {'fields': ['blog_date'], 'classes': ['collapse']}),
    ]

    inlines = [BlogInline]

    list_display = ('blog_text', 'blog_date', 'was_published_recently')

admin.site.register(Blog, BlogAdmin)