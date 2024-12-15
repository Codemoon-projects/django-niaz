from core.models import RefModel
from django.db import models
from django_jalali.db import models as jmodels
from django.conf import settings


class MessageType(models.IntegerChoices):
    INFO = 1, "اعلان"
    WARNING = 2, "هشدار"
    DANGER = 3, "خطر"
    EVENT = 4, "رویداد"


class Messagesmodel(RefModel):

    class Meta:
        verbose_name="پیام"
        verbose_name_plural="پیام ها"    
    

    title = models.CharField(
        max_length=255, 
        verbose_name="عنوان",
    )
    description = models.TextField(
        verbose_name="توضیحات",
    )
    type = models.IntegerField(
        choices=MessageType.choices,
        default=MessageType.INFO,
        verbose_name="نوع پیام",
    )
    date = models.DateTimeField(
        verbose_name="تاریخ",
    )
    badges = models.JSONField(
        verbose_name="نشان‌ها",
    )  # Storing array of strings as JSON
    user_can_delete = models.BooleanField(
        default=False, 
        verbose_name="قابل حذف توسط کاربر",
    )
    background = models.CharField(
        max_length=50, 
        blank=True, 
        null=True, 
        verbose_name="پس‌زمینه",
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='messages',
        verbose_name="کاربر"
    )

    def __str__(self):
        return self.title