from django.db import models

from apps.auth_user.models import User
from utils.models import SlugModel, BaseModel
from apps.books.models import Image, Category
from utils.slugify import slugify_field
from ckeditor.fields import RichTextField


# Create your models here.


class Events(SlugModel):
    image = models.ManyToManyField(Image,
                                   related_name='event_images',
                                   verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание',
                                   null=True, blank=True)
    category = models.ManyToManyField(Category,
                                      related_name='category_events',
                                      verbose_name='Категория')
    body = RichTextField(verbose_name='Текст',
                         null=True, blank=True)
    date = models.DateField(auto_now_add=True,
                            verbose_name='Дата')
    created_by = models.ForeignKey(User,
                                   on_delete=models.CASCADE,
                                   related_name='event_create_user',
                                   null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
