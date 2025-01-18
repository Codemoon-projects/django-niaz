from core.models import RefModel
from django.db import models
from models.drugstoresModel.city import CityModel
from models.drugstoresModel.peson import PersonModel
from django.core.validators import RegexValidator


class Drugstoresmodel(RefModel):

    class Meta:
        verbose_name="داروخانه"
        verbose_name_plural="داروخانه ها"
    
    image = models.ImageField(upload_to="drug/image", verbose_name="لوگو داروخانه", null=True, blank=True)
    
    name = models.CharField(

        max_length=100,
        verbose_name="نام داروخانه"
    )
    
    city = models.ForeignKey(
        CityModel,
        verbose_name="شهر", 
        on_delete=models.CASCADE)
    
    person = models.ForeignKey(
        PersonModel,
        verbose_name="شخص",
        on_delete=models.CASCADE)
    
    desc = models.TextField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="توضیحات"
    )
    
    phone1 = models.IntegerField(

        verbose_name="شماره تماس"
    )
    
    phone2 = models.IntegerField(

        null=True,
        blank=True,
        verbose_name="شماره تماس"

    )


    def __str__(self):
        return self.name