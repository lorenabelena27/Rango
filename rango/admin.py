from django.contrib import admin
import django


from rango.models import Category, Page,UserProfile

admin.site.register(Category)
admin.site.register(Page)
admin.site.register(UserProfile)
# Register your models here.
