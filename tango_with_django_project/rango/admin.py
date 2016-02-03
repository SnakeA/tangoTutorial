from django.contrib import admin
from rango.models import Category, Page


# This is to override the default "Page" display in the Admin interface
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

# Add in this class to customized the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

# Register your models here.
admin.site.register(Category,CategoryAdmin)
# In order to register the updated interface
admin.site.register(Page)


