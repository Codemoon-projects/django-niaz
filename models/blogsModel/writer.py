from core.models import RefModel
from django.db import models

class WriterModel(RefModel):
    class Meta:
        verbose_name = "نویسنده"
        verbose_name_plural = "نویسنده ها"
    
    name = models.CharField("نام نویسنده", max_length=100)
    

    def __str__(self):
        return self.name