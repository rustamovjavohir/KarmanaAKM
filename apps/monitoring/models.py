import requests
from django.db import models

from config import settings
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
    country = models.CharField(max_length=255,
                               verbose_name='Страна',
                               null=True, blank=True)
    region = models.CharField(max_length=255,
                              verbose_name='Регион',
                              null=True, blank=True)
    longitude = models.FloatField(max_length=255,
                                  verbose_name='Долгота',
                                  null=True, blank=True)
    latitude = models.FloatField(max_length=255,
                                 verbose_name='Широта',
                                 null=True, blank=True)

    def get_some_datas(self):
        params = {
            'ip': self.ip_address,
            'accessKey': settings.APIIP_KEY,
        }
        return requests.get(url=settings.APIIP_URL, params=params)

    def fill_data(self):
        if self.get_some_datas().status_code == 200:
            data = self.get_some_datas().json()
            self.country = data.get('countryName')
            self.region = data.get('regionName')
            self.longitude = data.get('longitude')
            self.latitude = data.get('latitude')
            self.save()

    def __str__(self):
        return self.ip_address

    class Meta:
        verbose_name = 'Tashrif buyurgan'
        verbose_name_plural = 'Tashrif buyurganlar'
