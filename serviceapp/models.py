from django.db import models

# Create your models here.

class ServiceCategory(models.Model):

    name = models.CharField('Имя категорий',max_length=255)
    img = models.ImageField('Фото',upload_to="ServiceCategoryImg/",null=True,blank=True)
    description = models.TextField('Описания категорий' ,null=True,blank=True)
    created_at = models.DateTimeField('Время созданий',auto_now=True)
    icon = models.CharField('Класс иконок',max_length=255,blank=True,null=True)

    def __str__(self):
        return f"{self.name} Создано: {self.created_at}"


class Service(models.Model):

    name = models.CharField('Имя сервиса',max_length=255)
    img = models.ImageField('Фото',upload_to="ServiceImg/",null=True,blank=True)
    description = models.TextField('Описания сервиса',null=True,blank=True)
    created_at = models.DateTimeField('Время созданий',auto_now=True)
    icon = models.CharField('Класс иконок',max_length=255,blank=True,null=True)
    category = models.ForeignKey(ServiceCategory,verbose_name="Категория сервиса",on_delete=models.CASCADE,related_name="services")

    def __str__(self):
        return f"{self.name} Создано: {self.created_at}"