from django.db import models

# Create your models here.

class Workers(models.Model):

    name = models.CharField('Фио',max_length=255)
    description = models.TextField('О работнике')
    img = models.ImageField('Фото',upload_to="Workers/")
    position = models.CharField('Должность',max_length=255)

    def __str__(self):

        return self.name

class DirectionCategory(models.Model):

    name = models.CharField('Название категорий направлений',max_length=255)
    icon = models.CharField('Иконка категорий направлений',max_length=255)
    img = models.ImageField('Фото категорий направлений',null=True,blank=True,upload_to="DirectionCatImg/")
    description = models.TextField('Описание категорий направлений')

    def __str__(self):

        return self.name

class Direction(models.Model):

    name = models.CharField('Название направлений',max_length=255)
    icon = models.CharField('Иконка направлений',max_length=255,null=True,blank=True)
    description = models.TextField('Описание направлений',null=True,blank=True)
    category = models.ForeignKey(DirectionCategory,verbose_name="Категорий направлений",on_delete=models.CASCADE,related_name="directions")

    def __str__(self):

        return self.name

class DirectionImg(models.Model):

    img = models.ImageField('Фото направлений',null=True,blank=True,upload_to="DirectionImg/")
    direction = models.ForeignKey(Direction,verbose_name="Фото направлений",on_delete=models.CASCADE,related_name="directionsimgs")

    def __str__(self):

        return self.direction.name