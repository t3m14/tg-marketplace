from django.db import models

class User(models.Model):
    ROLE_CHOICES = {
        'ADMIN': 'ADMIN',
        'WORKER': 'WORKER',
        'CUSTOMER' : 'CUSTOMER',
        'SUPPORT' : 'SUPPORT'
    }
    name = models.CharField(max_length=100, verbose_name='Имя')
    image = models.ImageField(upload_to='images/', null=True)
    image_id = models.CharField(max_length=128, verbose_name="Айди картинки в телеграм")
    description = models.TextField(verbose_name='Описание')
    user_tag = models.CharField(max_length=100, verbose_name='Тег')
    user_id = models.IntegerField(verbose_name='ID пользователя', unique=True)
    rating = models.IntegerField(default=0, verbose_name='Рейтинг', null=True)
    portfolio_link = models.CharField(max_length=200, verbose_name='Ссылка на портфолио', blank=True)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, default='CUSTOMER', verbose_name='Роль')

    def __str__(self):
        return self.name + " | " + str(self.user_id)