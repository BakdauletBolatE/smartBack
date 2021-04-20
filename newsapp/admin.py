from django.contrib import admin
from .models import NewsCategory,News
# Register your models here.


admin.site.register(News)
admin.site.register(NewsCategory)