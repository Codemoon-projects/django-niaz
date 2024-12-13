from core.models import RefModel
from django.db import models
from models.resomeModel.models import ResomeModel
from models.repotageModel.tags import TagModel
from ckeditor.fields import RichTextField

class OnvanChoice(models.IntegerChoices):
    
    CHOICE_1 = 1, 'تکنسین داروخانه'
    CHOICE_2 = 2, 'تکنسین آرایشی بهداشتی'
    CHOICE_3 = 3, 'صندوقدار'
    CHOICE_4 = 4, 'انبار دار'
    CHOICE_5 = 5, 'مسئول فنی'
    CHOICE_6 = 6, 'قائم مقام'
    CHOICE_7 = 7, 'کارآموز دارویی'
    CHOICE_8 = 8, 'کار آموز آرایشی و بهداشتی'



class genderType(models.IntegerChoices):
    CHOICE_0 = 0, 'مونث'
    CHOICE_1 = 1, 'مذکر'
    CHOICE_2 = 2, 'بدون اهمیت'

class nameMotabarType(models.IntegerChoices):
    CHOICE_0 = 0, 'دارد'
    CHOICE_1 = 1, 'ندارد'
    CHOICE_2 = 2, 'بدون اهمیت'

class nezamType(models.IntegerChoices):
    CHOICE_0 = 0, 'دارد'
    CHOICE_1 = 1, 'ندارد'
    CHOICE_2 = 2, 'بدون اهمیت'
    
class TimeSelect(models.IntegerChoices):
    FULL_TIME = 0, "تمام وقت"
    HALF_TIME = 1, "نیمه وقت"
    PART_TIME = 2, "پاره وقت"


class Repotagemodel(RefModel):

    class Meta:
        verbose_name="اگهی"
        verbose_name_plural="اگهی ها"
    
    gender = models.IntegerField(
        'جنسیت',
        choices=genderType.choices,
    )
    
    title = models.IntegerField(
        'عنوان',
        choices=OnvanChoice.choices,
    )
    

    nameMotabar = models.IntegerField(
        'نامه معتبر از دانشگاه',
        choices=nameMotabarType.choices,
    )
    
    nezam = models.IntegerField(
        'کارت نظام',
        choices=nezamType.choices,
    )    
    
    saatHamkari = models.IntegerField(
        verbose_name='ساعت همکاری',
        choices=TimeSelect.choices,
    )
    
    
    desc = RichTextField(
        verbose_name="توضیحات بلاگ",
        )
    
    show = models.BooleanField(
        verbose_name="تایید شده",
        default=False
    )
    
    price = models.CharField(
        max_length=100,
        verbose_name="قیمت"
    )
    
    
    fromKarfarma = models.ForeignKey(
        "user.Karfarmamodel",
        on_delete=models.CASCADE,
        verbose_name="ایجاد شده توسط"
    )


    fori = models.BooleanField(
        default=False,
        verbose_name="فوری"
    )


    def __str__(self):
        return f"{self.fromKarfarma}:{self.created_at}"


    @property
    def resumes(self):
        return ResomeModel.objects.filter(
            repotage_id = self.pk,
            show = 1
            )

    @property
    def city(self):
        return "اردبیل"

    @property
    def tags(self):
        return TagModel.objects.filter(
            repotage_id = self.pk
        ).values_list("name", flat=True)

    