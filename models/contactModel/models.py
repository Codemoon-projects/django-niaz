from core.models import RefModel
from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator


class Contactmodel(RefModel):

    class Meta:
        verbose_name="تیکت"
        verbose_name_plural="تیکت ها"
    
    phone = models.IntegerField(
        validators=[
            MaxValueValidator(9999999999),
            MinValueValidator(9000000000),
        ],

        verbose_name="شماره تماس"
    )
    
    
    
    name = models.CharField(
        max_length=100,
        verbose_name="نام و نام خانوادگی"


    )
    
    
    title = models.CharField(
        max_length=100,
        verbose_name="عنوان"
    )

    dec = models.CharField(
        max_length=10000,
        verbose_name="توضیحات"
    )

    def __str__(self):
        return f"{self.phone}   {self.name}"