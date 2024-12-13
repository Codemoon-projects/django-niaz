from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from models.messagesModel.models import Messagesmodel
from import_export.admin import ImportExportMixin
from models.repotageModel.models import Repotagemodel
from models.blogsModel.writer import WriterModel
from models.blogsModel.models import Blogsmodel
from models.blogsModel.category import CategoryModel
from models.drugstoresModel.peson import PersonModel
from models.drugstoresModel.city import CityModel
from models.contactModel.models import Contactmodel
from models.storesModel.models import Storesmodel
from models.drugstoresModel.models import Drugstoresmodel
from user.karjoModel import Karjomodel
from user.models import UsersType, AllUsers
from user.karfarmaModel import Karfarmamodel
from user.history import TransactionHistory
from django.db import models
from user.models import UsersSerializer
from django.contrib import admin
from datetime import datetime
from django.utils.safestring import mark_safe
from models.resomeModel.models import ResomeModel 
from models.repotageModel.tags import TagModel
from django import forms
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime


@admin.register(AllUsers)
class AdminPanel(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'username',
        'usertype',
        'active',
        'is_admin',
        'kifpool',
        'sms'
    ]
# --------------------------------------------------------- resomeModel
@admin.register(ResomeModel)
class ResomePanel(admin.ModelAdmin):

    @admin.display(description="کاربر")
    def karbar(self, obj):
        return f"{obj.user.fName} {obj.user.lName}"
    
    @admin.display(description="آگهی")
    def agahi(self, obj):
        return obj.repotage.title

    list_display = [
        'karbar',
        'agahi',
        'status',
        'show'
    ]
# --------------------------------------------------------- messagesModel
@admin.register(Messagesmodel)
class MessagesmodelPanel(ImportExportMixin, admin.ModelAdmin):
    @admin.display(description="انجام شده",boolean=True)
    def testtime(obj,self):
        today = datetime.now().date()
        print(today)
        print(self.time)
        if self.time <= today:
            return True
        else:
            return False
    list_display=['time', 'message', 'testtime']
    list_filter=['time']
# --------------------------------------------------------- repotageModel


class TagslInline(admin.TabularInline):
    model = TagModel
    verbose_name = 'برچسب'
    verbose_name_plural = "برچسب ها"
    fk_name = 'repotage'

    
@admin.register(Repotagemodel)
class RepotagemodelPanel(ImportExportMixin, admin.ModelAdmin):
    
    list_display=['title', 'price', 'desc' , 'show', 'price', 'fromKarfarma']
    list_filter=['fromKarfarma']  
    inlines = [TagslInline]
# --------------------------------------------------------- blogsModel
@admin.register(WriterModel)
class WriterModelPanel(ImportExportMixin, admin.ModelAdmin):
    def has_module_permission(self, request):
        return False

@admin.register(Blogsmodel)
class BlogsmodelPanel(ImportExportMixin, admin.ModelAdmin):
    # formfield_overrides = {
    #     RichTextField: {'widget': CkeditorWidget},
    # }



    def blog_image(self, obj):
        if obj.image.url is not None:
            return mark_safe(f'<img src="{obj.image.url}" height="400" width="400" />')
        else:
            return None


    readonly_fields = ['blog_image']
    fields=['image','blog_image','name','catgegory', 'writer', 'desc', 'blogText', 'better', 'readTime']
    list_display=['name', 'catgegory', 'writer', 'better', 'readTime']
    list_filter=['name', 'writer', 'catgegory']
    list_max_show_all=10
  
@admin.register(CategoryModel)
class categorypanel(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False

# --------------------------------------------------------- contactModel
@admin.register(Contactmodel)
class ContactmodelPanel(ImportExportMixin, admin.ModelAdmin):
    
    list_display=['title', 'dec', 'name', 'phone']
    list_filter=['phone', 'name']
# --------------------------------------------------------- storesModel
@admin.register(Storesmodel)
class StoresmodelPanel(ImportExportMixin, admin.ModelAdmin):
    
    """"""
# --------------------------------------------------------- drugstoresModel
@admin.register(Drugstoresmodel)
class DrugstoresmodelPanel(ImportExportMixin, admin.ModelAdmin):
    
    list_display=['__str__', 'city', 'person', 'phone1']
    list_filter=['city', 'name', 'person']
    
    
    # --------------------------------------------------------- drugstoresModel

@admin.register(PersonModel)
class PersonModelPanel(ImportExportMixin, admin.ModelAdmin):
    def has_module_permission(self, request):
        return False
    list_display=['__str__', 'phone']
    list_filter=['name']
# --------------------------------------------------------- drugstoresModel
@admin.register(CityModel)
class CityModelelPanel(ImportExportMixin, admin.ModelAdmin):
    def has_module_permission(self, request):
        return False
    list_display=['__str__']
    list_filter=['name']


#--------------------------------------- KARFARMAMODEL

class TestForm(forms.ModelForm):
    class Meta:
        model = Karfarmamodel
        fields = ['date']

    def __init__(self, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)
        self.fields['date'] = JalaliDateField(label=_('date'), 
            widget=AdminJalaliDateWidget 
        )

@admin.register(Karfarmamodel)
class KarfarmaPanel(admin.ModelAdmin):
    @admin.display(description="عکس بنر")
    def banner_image(self, obj):
        if obj.banner.url is not None:
            return mark_safe(f'<img src="{obj.banner.url}" height="400" width="400" />')
        else:
            return None
    @admin.display(description="عکس لوگو")
    def logo_image(self, obj):
        if obj.logo.url is not None:
            return mark_safe(f'<img src="{obj.logo.url}" height="400" width="400" />')
        else:
            return None

    @admin.display(description="نام")
    def name(obj, self):
        return self.name

    readonly_fields=['logo_image', 'banner_image']
    list_display=['name', 'placeName', 'phoneMajazi']
    fields=[
        'fName', 'lName', 'email',
        'banner_image', 'banner',
        'logo_image', 'logo',
        'noFaaliat',
        'address',
        'placeName', 'date',
        'website', 'rubika', 'phoneMajazi',
        'lat', 'long'
    ]
    forms='TestForm'
#--------------------------------------- KARFARMAMODEL USER ADMIN

@admin.register(TransactionHistory)
class TransActionHistoryPanel(admin.ModelAdmin):
    readonly_fields= ["user","price","vaziat","code"]

class KarfarmamodelInline(admin.StackedInline):
    model = Karfarmamodel
    can_delete = False
    verbose_name = 'کارفرما'
    verbose_name_plural = "کارفرما"
    fk_name = 'user'
    min_num = 1
    max_num = 1
    


class KarfarmamodelPanel(UserAdmin):
    inlines = (KarfarmamodelInline, )
    list_display = ["username"]
    list_filter = ["active"]
    
    fieldsets = (
        ("اطلاعات یوزر", {"fields": ("username", "password", )}),
    )
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.usertype = UsersType.KARFARMA_MODEL
        super().save_model(request, obj, form, change)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(usertype=UsersType.KARFARMA_MODEL)

    def get_inline_instances(self, request, obj=None):
        return super(KarfarmamodelPanel, self).get_inline_instances(request, obj)


class KarfarmamodelProxy(AllUsers):
    
    class Meta:
        proxy = True
        verbose_name="کارفرما"
        verbose_name_plural = 'کارفرما ها'
	
admin.site.register(KarfarmamodelProxy, KarfarmamodelPanel)



#--------------------------------------KARJO-------------

@admin.register(Karjomodel)
class KarjomodelPanel(ImportExportMixin, admin.ModelAdmin):

    @admin.display(description="فایل تحصیلات")
    def education_file_image(self, obj):
        if obj.education_file.url is not None:
            return mark_safe(f'<img src="{obj.education_file.url}" height="400" width="400" />')
        else:
            return None

    @admin.display(description="فایل سابقه کاری")
    def worked_image(self, obj):
        if obj.worked_file.url is not None:
            return mark_safe(f'<img src="{obj.worked_file.url}" height="400" width="400" />')
        else:
            return None

    @admin.display(description="فایل کارت ملی")
    def meliNo_image(self, obj):
        if obj.meliNo_file.url is not None:
            return mark_safe(f'<img src="{obj.meliNo_file .url}" height="400" width="400" />')
        else:
            return None

    @admin.display(description="فایل تکنسین")
    def technisian_file_image(self, obj):
        if obj.technisian_file.url is not None:
            return mark_safe(f'<img src="{obj.technisian_file.url}" height="400" width="400" />')
        else:
            return None

    @admin.display(description="فایل گواهی مرتبط")
    def certificate_file_image(self, obj):
        if obj.certificate_file.url is not None:
            return mark_safe(f'<img src="{obj.certificate_file.url}" height="400" width="400" />')
        else:
            return None
    
    @admin.display(description="فایل گواهی عدم سو پیشینه")
    def badBack_file_image(self, obj):
        if obj.badBack_file.url is not None:
            return mark_safe(f'<img src="{obj.badBack_file.url}" height="400" width="400" />')
        else:
            return None

    @admin.display(description="فایل ساعات بازآموزی")
    def retrain_file_image(self, obj):
        print(obj.saatBazAmozy_file.url)
        if obj.retrain_file.url is not None:
            return mark_safe(f'<img src="{obj.retrain_file.url}" height="400" width="400" />')
        else:
            return None



    readonly_fields=[
    'education_file_image',
    'worked_image',
    'meliNo_image',
    'technisian_file_image',
    'certificate_file_image',
    'badBack_file_image',
    'retrain_file_image'
            ]


    fields=[
    'type', 'fName', 'lName', 'birthdate', 'gender',
    'lat','long',
    'education', 'education_file', 'education_file_image',
    'worked', 'worked_file', 'worked_image',
    'nezam',
    'meliNo_file', 'meliNo_image', 'meliNo',
    'referralCode',
    'knowType',
    'technisian', 'technisian_file', 'technisian_file_image',
    'certificate', 'certificate_file', 'certificate_file_image',
    'program',
    'badBack', 'badBack_file', 'badBack_file_image',
    'retrain', 'retrain_file', 'retrain_file_image',
            ]

    list_display=[
        '__str__',
        'meliNo',
        'gender',
        'education',
        'nezam',
        'worked'
            ]

    list_filter=['meliNo']
    list_max_show_all=10


#--------------------------------------- KARJOMODEL USER ADMIN
# 

class karjomodelInline(admin.StackedInline):
    model = Karjomodel
    can_delete = False
    verbose_name = 'کارجو'
    verbose_name_plural = "کارجو"
    fk_name = 'user'
    min_num = 1
    max_num = 1
    


class karjomodelPanel(UserAdmin):
    inlines = (karjomodelInline, )
    list_display = ["username"]
    list_filter = ["active"]
    
    fieldsets = (
        ("اطلاعات یوزر", {"fields": ("username", "password", )}),
    )
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.usertype = UsersType.KARJO_MODEL
        super().save_model(request, obj, form, change)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(usertype=UsersType.KARJO_MODEL)

    def get_inline_instances(self, request, obj=None):
        return super(karjomodelPanel, self).get_inline_instances(request, obj)


class KarjomodelProxy(AllUsers):
    
    class Meta:
        proxy = True
        verbose_name="کارجو"
        verbose_name_plural = 'کارجو ها'
	
admin.site.register(KarjomodelProxy, karjomodelPanel)