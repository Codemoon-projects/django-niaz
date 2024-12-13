from core.models import RefModel
from django.db import models

class TagModel(RefModel):
    class Meta:
        verbose_name="برچسب"
        verbose_name_plural="برچسب ها"

    name = models.CharField(max_length=100, verbose_name="نام تگ")
    repotage = models.ForeignKey("repotageModel.Repotagemodel", verbose_name="آگهی مرتبط", on_delete=models.CASCADE)


    def __str__(self):
        return self.name
