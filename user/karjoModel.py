from core.models import RefModel
from django.db import models
from django.conf import settings
from django_jalali.db import models as jmodels




class Type(models.IntegerChoices):
    
    CHOICE_0 = 0, 'تکنسین داروخانه'
    CHOICE_1 = 1, 'تکنسین آرایشی بهداشتی'
    CHOICE_2 = 2, 'صندوقدار'
    CHOICE_3 = 3, 'انبار دار'
    CHOICE_4 = 4, 'مسئول فنی'
    CHOICE_5 = 5, 'قائم مقام'
    CHOICE_6 = 6, 'کارآموز دارویی'
    CHOICE_7 = 7, 'کار آموز آرایشی و بهداشتی'

class genderType(models.IntegerChoices):
    
    CHOICE_1 = 0, 'زن'
    CHOICE_0 = 1, 'مرد' 

class tahsilatType(models.IntegerChoices):
    
    CHOICE_0 = 0, 'دانشجو'
    CHOICE_1 = 1, 'سیکل'
    CHOICE_2 = 2, 'دیپلم'
    CHOICE_3 = 3, 'کارشناسی'
    CHOICE_4 = 4, 'ارشد'
    CHOICE_5 = 5, 'دکتری'
    
class nezamType(models.IntegerChoices):
    
    CHOICE_0 = 0, 'معاف'
    CHOICE_1 = 1, 'مشمول'
    CHOICE_2 = 2, 'پایان خدمت'
    
class ashnaiiType(models.IntegerChoices):
    
    CHOICE_0 = 0, 'معرف'
    CHOICE_1 = 1, 'در داروخانه'
    CHOICE_2 = 2, "گوگل"
    
    
class narmAfzarType(models.IntegerChoices):
    
    CHOICE_0 = 0, 'ایمن افزار شایگان'
    CHOICE_1 = 1, 'قانون فارما'
    CHOICE_2 = 2, 'فارماسی'
    CHOICE_3 = 3, 'دارو پردازان'
    CHOICE_4 = 4, 'ماندگار'
    CHOICE_5 = 5, 'وکیل'

    
class SelectChoicesType(models.IntegerChoices):

    NO = 0, 'خیر'
    YES = 1, 'بله'


class Karjomodel(RefModel):

    class Meta:
        verbose_name="کارجو"
        verbose_name_plural="کارجو ها"
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    type = models.IntegerField(
        'عنوان شغلی خود را انتخاب کنید',
        choices=Type.choices,
    )

    profilePicture = models.FileField(
        verbose_name="لوگو",
        upload_to="static/karjo/logo_file",
        null=True,
        blank=True
    )
    
    
    fName = models.CharField(
        max_length=100,
        verbose_name="نام"
    )
    
    lName = models.CharField(
        max_length=100,
        verbose_name="نام خانوادگی"
    )
    
    birthdate = jmodels.jDateField(
        verbose_name="تاریخ تولد",
        null=True,
        blank=True
    )
    
    
    gender = models.IntegerField(
        'جنسیت',
        choices=genderType.choices,
    )
    
    
    lat = models.FloatField(verbose_name=" طول جغرافیایی",null=True,blank=True
    )
    long = models.FloatField(verbose_name=" عرض جغرافیایی",null=True,blank=True
    )
    
    education = models.IntegerField(
        'وضعیت تحصیلات',
        choices=tahsilatType.choices,
        null=True,
        blank=True
    )
    
    
    education_file = models.FileField(
        null=True,blank=True,
        verbose_name="تحصیلات",
        upload_to="static/tahsilat_file_file",
    )
    
    
    worked = models.IntegerField(
        'آیا سابقه کار دارید؟',
        choices=SelectChoicesType.choices,
        null=True,
        blank=True
    )
    
    
    
    worked_file = models.FileField(
        null=True,blank=True,
        verbose_name="سابقه کار",
        upload_to="static/worked_file_file",
    )
    
    
    nezam = models.IntegerField(
        'وضعیت نظام وظیفه',
        choices=nezamType.choices,
        null=True,
        blank=True
    )
    
    
    nezam_file = models.FileField(
        null=True,blank=True,
        upload_to="static/nezam_file_file",
        verbose_name="کارت نظام وظیفه"
    )
    
    meliNo_file = models.FileField(
        null=True,blank=True,
        upload_to="static/meliNo_file_file",
        verbose_name="کارت ملی"
    )
    
    
    meliNo = models.CharField(
        max_length=100,
        verbose_name="کد ملی",
        null=True,
        blank=True
    )
    
    
    referralCode = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="معرف"
    )
    
    knowType = models.IntegerField(
        'نحوه‌ی آشنایی با سایت',
        choices=ashnaiiType.choices,
        null=True,
        blank=True
    )
    
    
    technician = models.IntegerField(
        'آیا دارای گواهی تکنسین دارویی یا آرایشی بهداشتی هستید ؟ ',
        choices=SelectChoicesType.choices,
        null=True,
        blank=True
    )
    
    technician_file = models.FileField(
        null=True,blank=True,
        verbose_name="گواهی تکنسین",
        upload_to="static/teknesian_file_file",
    )
    
    
    certificate = models.IntegerField(
        'آیا دارای گواهی مرتبط هستید ؟',
        choices=SelectChoicesType.choices,
        null=True,
        blank=True
    )
    
    
    certificate_file = models.FileField(
        null=True,blank=True,
        verbose_name="گواهی مرتبط",
        upload_to="static/mortabet_file_file",
    )
    
    
    
    program = models.IntegerField(
        'در صورت آشنایی با نرم‌افزار مرتبط، آن را انتخاب کنید ',
        choices=narmAfzarType.choices,
        null=True,
        blank=True
    )
    
    
    badBack = models.IntegerField(
        'آیا دارای گواهی عدم سو پیشینه هستید ؟',
        choices=SelectChoicesType.choices,
        null=True,
        blank=True
    )
    
    badBack_file = models.FileField(
        null=True,blank=True,
        verbose_name='عدم سو پیشینه',
        upload_to="static/soPishine_file_file",
    )
    
    
    retrain = models.IntegerField(
        'آیا دارای ساعات بازآموزی معتبر هستید ؟',
        choices=SelectChoicesType.choices,
        null=True,
        blank=True
    )
    
    retrain_file = models.FileField(
        null=True,blank=True,
        verbose_name="ساعات بازآموزی معتبر",
        upload_to="static/retrain_file",
    )
    
    

    def __str__ (self):
        return f"{self.fName}  {self.lName}"