from ckeditor.fields import RichTextField
from django.db import models

from apps.books.models import Image
from apps.auth_user.models import User
from utils.models import SlugModel


class Writers(SlugModel):
    name = models.CharField(max_length=255, verbose_name="Ismi")
    description = RichTextField(verbose_name='Ma\'lumot',
                                null=True, blank=True)
    image = models.ManyToManyField(Image,
                                   related_name='writer_images',
                                   verbose_name='Rasmlar')
    created_by = models.ForeignKey(User,
                                   on_delete=models.CASCADE,
                                   related_name='writer_created_by',
                                   verbose_name='Yaratuvchi')

    class Meta:
        verbose_name = "Ijodkor"
        verbose_name_plural = "Ijodkorlar"

    def __str__(self):
        return self.name
