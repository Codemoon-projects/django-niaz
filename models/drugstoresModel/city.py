from core.models import RefModel
from django.db import models


class CityModel(RefModel):
    class Meta:
        verbose_name="شهر"
        verbose_name_plural="شهر ها"
    name = models.CharField(
        "نام شهر",
        max_length=100,)
    

    def __str__(self):
        return self.name