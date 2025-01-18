from core.models import RefModel
from django.db import models


class Banner(RefModel):
    class Meta:
        verbose_name="بنر صفحه اصلی"
        verbose_name_plural="بنر صفحه اصلی"
    
    name = models.CharField(max_length=100, verbose_name="نام بنر")
    image = models.ImageField(verbose_name="بنر های پیشنهاد ویژه")


    def __str__(self):
        return self.name