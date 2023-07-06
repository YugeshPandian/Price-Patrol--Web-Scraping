from django.contrib import admin
from .models import *


class TrendingAdmin(admin.ModelAdmin):
    list_display=('name','image','description')

admin.site.register(Trending,TrendingAdmin)
# Register your models here.

