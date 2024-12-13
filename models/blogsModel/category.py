from core.models import RefModel
from django.db import models

class CategoryModel(RefModel):
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
    
    name = models.CharField("نام دسته بندی ", max_length=100)


    def __str__(self):
        return self.name
    
    
    