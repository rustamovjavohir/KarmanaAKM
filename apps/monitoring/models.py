from django.db import models
from utils.models import BaseModel


# Create your models here.

class Visitors(BaseModel):
    ip_address = models.CharField(max_length=255, verbose_name='IP адрес')
    user_agent = models.CharField(max_length=255,
                                  verbose_name='User Agent',
                                  blank=True, null=True)
    path = models.CharField(max_length=255,
                            verbose_name='Путь',
                            null=True, blank=True)
    method = models.CharField(max_length=255,
                              verbose_name='Метод',
                              null=True, blank=True)
    status_code = models.CharField(max_length=255,
                                   verbose_name='Статус код',
                                   null=True, blank=True)
    query_string = models.CharField(max_length=255,
                                    verbose_name='Строка запроса',
                                    null=True, blank=True)

    class Meta:
        verbose_name = 'Tashrif buyurgan'
        verbose_name_plural = 'Tashrif buyurganlar'
