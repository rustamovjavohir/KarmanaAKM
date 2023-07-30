from django.db import models

from apps.auth_user.models import User
from utils.models import SlugModel, BaseModel


class Image(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название')
    image = models.ImageField(upload_to='images', verbose_name='Изображение')
    is_main = models.BooleanField(default=False, verbose_name='Главное?')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return self.image.url

    def save_base(
            self,
            raw=False,
            force_insert=False,
            force_update=False,
            using=None,
            update_fields=None,
    ):
        image_name = f"{self.name}.{self.image.name.split('.')[-1]} " if self.name else self.image.name
        self.image.name = image_name
        return super().save_base(
            raw=False,
            force_insert=False,
            force_update=False,
            using=None,
            update_fields=None,
        )


class Author(SlugModel):
    name = models.CharField(max_length=255,
                            verbose_name='Имя')
    image = models.ManyToManyField(Image,
                                   related_name='author_images',
                                   verbose_name='Изображение')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.name


class Category(SlugModel):
    name = models.CharField(max_length=255,
                            verbose_name='Название')
    parent = models.ForeignKey('self', blank=True, null=True,
                               related_name='children',
                               on_delete=models.CASCADE,
                               verbose_name='Родительская категория')

    image = models.ManyToManyField(Image,
                                   related_name='category_images',
                                   verbose_name='Изображение')
    is_event = models.BooleanField(default=False,
                                   verbose_name='Событие?')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Book(SlugModel):
    name = models.CharField(max_length=255,
                            verbose_name='Название')
    image = models.ManyToManyField(Image,
                                   related_name='book_images',
                                   verbose_name='Изображение')

    author = models.ManyToManyField(Author,
                                    related_name='author_books',
                                    verbose_name='Автор')
    category = models.ManyToManyField(Category,
                                      related_name='category_books',
                                      verbose_name='Категория')
    description = models.TextField(null=True, blank=True,
                                   verbose_name='Описание')
    created_by = models.ForeignKey(User,
                                   on_delete=models.CASCADE,
                                   related_name='book_create_user',
                                   null=True, blank=True,
                                   verbose_name='Создатель')

    def __str__(self):
        return self.name
