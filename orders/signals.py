from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Order
from robots.models import Robot


@receiver(post_save, sender=Robot)
def notify_clients(sender, instance, created, **kwargs):
    """ Уведомляет клиентов, если робот появился в наличии"""
    if created:
        orders = Order.objects.filter(robot_serial=instance.serial)
        for order in orders:
            send_mail(
                subject='Ваш робот появился в наличии!',
                message=(
                    f'Добрый день!\n'
                    f'Недавно вы интересовались нашим роботом модели '
                    f'{instance.model}, версии {instance.version}.\n'
                    f'Этот робот теперь в наличии. '
                    f'Если вам подходит этот вариант - '
                    f'пожалуйста, свяжитесь с нами.'
                ),
                from_email='no-reply@robots.com',
                recipient_list=[order.customer.email]
                )