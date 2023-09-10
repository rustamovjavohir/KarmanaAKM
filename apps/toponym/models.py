from django.db import models
from ckeditor.fields import RichTextField

from apps.books.models import Image
from apps.auth_user.models import User
from utils.models import SlugModel


class Toponym(SlugModel):
    meaning = models.CharField(max_length=255,
                               null=True, blank=True,
                               verbose_name="Ma'nosi")
    description = RichTextField(verbose_name='Ma\'lumot',
                                null=True, blank=True)
    image = models.ManyToManyField(Image,
                                   related_name='toponym_images',
                                   verbose_name='Rasmlar')
    created_by = models.ForeignKey(User,
                                   on_delete=models.CASCADE,
                                   related_name='toponym_created_by',
                                   verbose_name='Yaratuvchi')

    class Meta:
        verbose_name = "Toponim"
        verbose_name_plural = "Toponimlar"

    @property
    def main_image(self):
        try:
            return self.image.filter(is_main=True).first().image.url
        except AttributeError:
            return None
