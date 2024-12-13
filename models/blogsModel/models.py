from core.models import RefModel
from django.db import models
from models.blogsModel.writer import WriterModel
from models.blogsModel.category import CategoryModel
from models.blogsModel.comments import Comment
from ckeditor.fields import RichTextField

class Blogsmodel(RefModel):

    class Meta:
        verbose_name = "بلاگ"
        verbose_name_plural = "بلاگ ها"
    
    image = models.ImageField(
        verbose_name="عکس بلاگ",
        upload_to="static/blogsPhoto")
    
    
    name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="نام بلاگ")
    
    catgegory = models.ForeignKey(
        CategoryModel,
        on_delete=models.RESTRICT,
        verbose_name="دسته بندی",
        null=True)
    
    writer = models.ForeignKey(
        WriterModel,
        on_delete=models.CASCADE,
        verbose_name="نویسنده",
        null=True)

    desc = models.TextField(
        max_length=100000,
        null=True,
        blank=True,
        verbose_name="چکیده ")    
    
    blogText = RichTextField(
        verbose_name="توضیحات بلاگ",
        )
    
    
    better = models.BooleanField(
        verbose_name="نمایش در صفحه اصلی",
        default=False)
    
    readTime = models.IntegerField(
        verbose_name="زمان خواندن",
        help_text="""
        با تنظیم این مقدار به شکل دقیقه میتوانید مخاطبین را به 
        وبلاگ خاص سوق دهید""")
    
    @property
    def comments(self):
        return Comment.objects.filter(blog_id=self.pk)
    
    @property
    def commentsCount(self):
        return self.comments.count()


    def __str__(self):
        return self.name