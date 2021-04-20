# Generated by Django 3.2 on 2021-04-11 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя категорий')),
                ('img', models.ImageField(upload_to='ServiceCategoryImg/', verbose_name='Фото')),
                ('description', models.TextField(verbose_name='Описания категорий')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Время созданий')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя сервиса')),
                ('img', models.ImageField(upload_to='ServiceImg/', verbose_name='Фото')),
                ('description', models.TextField(verbose_name='Описания сервиса')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Время созданий')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serviceapp.servicecategory', verbose_name='Категория сервиса')),
            ],
        ),
    ]