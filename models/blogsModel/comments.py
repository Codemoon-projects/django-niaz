from core.models import RefModel
from django.db import models


class Comment(RefModel):
    class Meta:
        verbose_name = "کامت"
        verbose_name_plural = "کامت ها"
    
    name = models.CharField(
        max_length=100,
        verbose_name="نام نویسنده نظر")
    
    email = models.CharField(
        max_length=100,
        verbose_name="ایمیل نویسنده نظر")
    
    desc = models.TextField(
        max_length=100000,
        verbose_name="متن نظر")
    
    blog = models.ForeignKey(
        "blogsModel.Blogsmodel",
        on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    
    