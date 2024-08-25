from typing import Any
from django.db import models
import uuid
from django.core.validators import MaxLengthValidator, MinLengthValidator
from pathlib import Path


class Page(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    title = models.CharField(
        max_length=100, 
        validators=[MaxLengthValidator(100)], 
        verbose_name="タイトル"
    )
    body = models.TextField(
        max_length=2000, 
        verbose_name="本文"
    )
    page_date = models.DateField(
        verbose_name="日付"
    )
    picture = models.ImageField(
        upload_to="diary/picture/",
        blank=True,
        null=True,
        verbose_name="写真"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="作成日時"
    )
    update_at = models.DateTimeField(
        auto_now=True, 
        verbose_name="更新日時"
    )

    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        pictuer = self.picture
        super().delete(*args, **kwargs)
        if pictuer:
            Path(pictuer.path).unlink(missing_ok=True)