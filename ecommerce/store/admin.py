from django.contrib import admin
from django.utils.html import format_html
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price', 'image_tag') 
    
    def image_tag(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" width="50" height="50"/>')
        return "No Image"
    image_tag.short_description = "Image"

admin.site.register(Product , ProductAdmin)
