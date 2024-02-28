from django.db import models
from users.models import User
from feed.models import Order, Service


class Offer(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    worker = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Работник')
    is_accepted = models.BooleanField(default=False, verbose_name='Принято')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    def __str__(self):
        return "Предложение" - self.order.title

class Deal(models.Model):
    STATUS_CHOICES = {
        #обсуждаются детали
        'OPEN': 'OPEN',
        #покупатель принял предложение
        'ACCEPTED': 'ACCEPTED',
        #покупатель отказался от предложения
        'DECLINED': 'DECLINED',
        #есть спор
        'DISPUTED': 'DISPUTED',
        #предложение закрыто
        'CLOSED': 'CLOSED'
    }
    worker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='worker_deals', verbose_name='Работник') 
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_deals', verbose_name='Покупатель') 
    deadline = models.DateTimeField(verbose_name='Срок') 
    status = models.CharField(max_length=100, verbose_name='Статус', choices=STATUS_CHOICES, default='OPEN')