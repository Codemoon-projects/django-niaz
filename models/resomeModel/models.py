from django.db import models
from core.models import RefModel
from ckeditor.fields import RichTextField
from django_jalali.db import models as jmodels


# Create your models here.

class ShowType(models.IntegerChoices):
    CHOICE_0 = 0, 'رد' 
    CHOICE_1 = 1, 'تایید'


class StatusType(models.IntegerChoices):
    CHOICE_0 = 0, 'قبول نشده'
    CHOICE_1 = 1, 'قبول شده'
    CHOICE_2 = 2, 'دیده نشده'
    CHOICE_3 = 3, 'دیده شده'




class ResomeModel(RefModel):

    class Meta:
        verbose_name = "رزومه"
        verbose_name_plural = "رزومه ها"

    show = models.IntegerField(
        'تایید یا رد',
        choices=ShowType.choices,
        default=0
    )
    
    status = models.IntegerField(
        'وضعیت',
        choices=StatusType.choices,
        default=0
    )
    desc = RichTextField(verbose_name="متن")
    repotage = models.ForeignKey("repotageModel.Repotagemodel", on_delete=models.CASCADE, verbose_name="پروژه")
    user = models.ForeignKey("user.Karjomodel", on_delete=models.CASCADE, verbose_name="کاربر")
    datetime = jmodels.jDateTimeField(verbose_name="تاریخ مصاحب", null=True, blank=True)


    def __str__(self):
        return f"{self.repotage}  {self.user}"

