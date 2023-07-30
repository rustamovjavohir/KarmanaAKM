from django.db import models
from utils.models import BaseModel, SlugModel


# Create your models here.

class Messages(BaseModel):
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    title = models.CharField(max_length=255, verbose_name='Название')
    email = models.EmailField(verbose_name='Email')
    body = models.TextField(verbose_name='Сообщение')
