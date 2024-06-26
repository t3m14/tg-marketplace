# Generated by Django 5.0.2 on 2024-02-28 09:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0003_alter_user_portfolio_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название главы')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название категории')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.chapter', verbose_name='Глава')),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название подкатегории')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.category', verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('is_published', models.BooleanField(default=False, verbose_name='Опубликовано')),
                ('is_top', models.BooleanField(default=False, verbose_name='Топ')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user', verbose_name='Работник')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.subcategory', verbose_name='Подкатегория')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('deadline', models.DateTimeField(verbose_name='Срок')),
                ('is_published', models.BooleanField(default=False, verbose_name='Опубликовано')),
                ('is_top', models.BooleanField(default=False, verbose_name='Топ')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user', verbose_name='Работник')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.subcategory', verbose_name='Подкатегория')),
            ],
        ),
    ]
