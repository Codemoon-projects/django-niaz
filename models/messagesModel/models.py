from core.models import RefModel
from django.db import models
from django_jalali.db import models as jmodels
from django.conf import settings


class MessageType(models.IntegerChoices):
    ELAN = 1, "اعلان"
    WARNING = 2, "هشدار"
    DANGER = 3, "خطر"
    EVENT = 4, "رویداد"


class Messagesmodel(RefModel):

    class Meta:
        verbose_name="رویداد"
        verbose_name_plural="رویداد ها"    
    
    time = jmodels.jDateField(
        verbose_name="زمان",
        null=True, 
        blank=True,
    )
    
    
    type = models.IntegerField(
        "نوع اعلان",
        choices=MessageType.choices
    )
    
    title = models.CharField(
        "عنوان پیام",
        max_length=200
    )

    message = models.TextField(
        max_length=10000,
        verbose_name="متن پیام",
        null=True, 
        blank=True
    )

    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.message} {self.time}"