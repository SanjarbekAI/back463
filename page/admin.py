from django.contrib import admin

from page.models import NewsModel, PopularTourModel, DestinationModel, EmailModel


@admin.register(NewsModel)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']


@admin.register(DestinationModel)
class DestinationModelAdmin(admin.ModelAdmin):
    list_display = ['country', 'city', 'created_at']
    search_fields = ['city', 'country']
    list_filter = ['created_at', 'updated_at']


@admin.register(PopularTourModel)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'days', 'price']


@admin.register(EmailModel)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ['email', 'created_at']
    search_fields = ['email']
    list_filter = ['created_at']
