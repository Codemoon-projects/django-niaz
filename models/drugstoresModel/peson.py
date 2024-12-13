from core.models import RefModel
from django.db import models
from django.core.validators import RegexValidator



class PersonModel(RefModel):
    class Meta:
        verbose_name="شخص"
        verbose_name_plural="اشخاص"
    
    name = models.CharField("نام شخص", max_length=50)
    phone = models.IntegerField(
        validators=[RegexValidator(
            regex= r"^(?:0|98|98|980|0098|098|00980)?(9\d{9})$"
        )],
        verbose_name="شماره تماس"

    )
    def __str__(self):
        return self.name
    