from core.models import RefModel
from django.db import models


class Storesmodel(RefModel):
    class Meta:
        verbose_name="داروخانه"
        verbose_name_plural="داروخانه ها"
    
    
    name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )


    def __str__(self):
        return self.name