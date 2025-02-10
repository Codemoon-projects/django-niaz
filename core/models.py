from django.db import models
from django_jalali.db import models as jmodels

class RefModel(models.Model):
    created_at = jmodels.jDateField(
        auto_now=True, editable=False, verbose_name="تاریخ ایجاد"
    )

    class Meta:
        abstract = True


class Tablig(models.Model):
    class Meta:
        verbose_name="تبلیغات ویژه"
        verbose_name_plural="تبلیغات ویژه"
    name = models.CharField(max_length=100, verbose_name="نام")
    desc = models.CharField(max_length=1000, verbose_name="توضیحات")
    image = models.ImageField(verbose_name="عکس تبلیغ", help_text="بنر با طول تمام صفحه قرار حواهد گرفت.")
    link = models.CharField(max_length=1000, verbose_name="لینک تبلیغ")