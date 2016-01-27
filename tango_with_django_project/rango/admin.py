from django.contrib import admin
from rango.models import Category, Page


# This is to override the default "Page" display in the Admin interface
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

# Register your models here.
admin.site.register(Category)
# In order to register the updated interface
admin.site.register(Page, PageAdmin)
