from django.db import models

# Create your models here.

class NewsCategory(models.Model):

    name = models.CharField('Имя категорий',max_length=255)
    img = models.ImageField('Фото',upload_to="NewsCategoryImg/")
    description = models.TextField('Описания категорий')
    created_at = models.DateTimeField('Время созданий',auto_now=True)

    def __str__(self):
        return f"{self.name} Создано: {self.created_at}"


class News(models.Model):

    title = models.CharField('Загаловок новости',max_length=255)
    img = models.ImageField('Фото',upload_to="NewsImg/")
    description = models.TextField('Описания новости')
    created_at = models.DateTimeField('Время созданий',auto_now=True)
    category = models.ForeignKey(NewsCategory,verbose_name="Категория новости",on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} Создано: {self.created_at}"
