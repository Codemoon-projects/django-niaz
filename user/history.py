from django.db import models
from user.models import AllUsers

class StatusType(models.IntegerChoices):
    
    CHOICE_0 = 0, 'ناموفق'
    CHOICE_1 = 1, 'موفق'

class TransactionHistory(models.Model):

    class Meta:
        verbose_name = "تراکنش"
        verbose_name_plural = "تراکنش ها"


    user = models.ForeignKey(AllUsers, on_delete=models.RESTRICT, verbose_name="کاربر")
    price = models.IntegerField(verbose_name="مبلغ")
    vaziat = models.IntegerField(
        'وضعیت پرداخت',
        choices=StatusType.choices,
        default=0
        )
    code = models.CharField(max_length=100, verbose_name="کد درگاه")

    def __str__(self):
        return f"{self.user} ({self.price}) {self.code}"