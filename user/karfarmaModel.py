from core.models import RefModel
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django_jalali.db import models as jmodels




class NoFaaliatType(models.IntegerChoices):
    
    DRUGSTORE_DOCTOR = 0, 'دکتر داروساز داروخانه'
    DRUGSTORE_PERSON = 1, 'مسئول فنی داروخانه'
    COMPANY_DOCTOR = 2, 'دکتر داروساز شرکت پخش'
    COMPANY_PERSON = 3, 'بازاریاب شرکت پخش'


class Karfarmamodel(RefModel):
    class Meta:
        verbose_name="کارفرما"
        verbose_name_plural="کارفرما ها "    
    
    banner = models.FileField(
        verbose_name="بنر",
        upload_to="static/banner_file",
        null=True,
        blank=True
    )

    logo = models.FileField(
        verbose_name="لوگو",
        upload_to="static/logo_file",
        null=True,
        blank=True
    )
    
    fName=models.CharField(
        max_length=100,
        verbose_name="نام"
    )

    lName=models.CharField(
        max_length=100,
        verbose_name="نام خانوادگی"
    )

    email = models.EmailField(verbose_name="ایمیل کارفرما", null=True)
    
    
    noFaaliat = models.IntegerField(
        'نوع کارفرما',
        choices=NoFaaliatType.choices,
    )
    
    
    address = models.CharField(
        verbose_name="ادرس",
        max_length=1000,
    )
    
    
    placeName = models.CharField(
        verbose_name="نام موسسه",
        max_length=100,
        null=True,
        blank=True,
    )
    
 
    
    date = jmodels.jDateField(verbose_name="تاریخ تاسیس", null=True)
    
    
    website = models.CharField(
        verbose_name="ادرس سایت",
        max_length=100,
        null=True,
        blank=True,
    )
    
    
    rubika = models.CharField(
        verbose_name="ادرس روبیکا",
        max_length=100,
        null=True,
        blank=True,
    )
    
    
    
    phoneMajazi = models.IntegerField(
        verbose_name="شماره تلفن مجازی",
        validators=[
            MinValueValidator(9000000000),
            MaxValueValidator(9999999999)
        ],
        null=True,
        blank=True,
    )
    
    lat = models.FloatField(verbose_name="طول جغرافیایی", null=True, blank=True)
    
    long = models.FloatField(verbose_name="عرض جغرافیایی", null=True, blank=True)
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username)

    @property
    def name(self):
        return f"{self.fName} {self.lName}"