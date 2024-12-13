from django.db import models
from django_jalali.db import models as jmodels

class RefModel(models.Model):
    created_at = jmodels.jDateField(
        auto_now=True, editable=False, verbose_name="تاریخ ایجاد"
    )

    class Meta:
        abstract = True
