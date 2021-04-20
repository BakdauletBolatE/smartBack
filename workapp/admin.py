from django.contrib import admin
from .models import Workers,Direction,DirectionCategory,DirectionImg
# Register your models here.

admin.site.register(Workers)


class DirectionImgTabularInline(admin.TabularInline):

    model = DirectionImg


class DirectionAdmin(admin.ModelAdmin):

    list_display = ('id','name')

    inlines = [
        DirectionImgTabularInline,
    ]



admin.site.register(Direction,DirectionAdmin)

admin.site.register(DirectionImg)


class DirectionCategoryAdmin(admin.ModelAdmin):

    list_display = ('id','name')

admin.site.register(DirectionCategory,DirectionCategoryAdmin)