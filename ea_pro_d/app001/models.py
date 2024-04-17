# Create your models here.
from django.db import models


class SymbolModel(models.Model):

    symbol = models.CharField(max_length=32, help_text="股票代码，如 'AAPL'")
    datatime = models.DateTimeField(auto_now_add=True, help_text="记录日期")
    OPrice = models.DecimalField(max_digits=8, decimal_places=4, help_text="开盘价")
    LPrice = models.DecimalField(max_digits=8, decimal_places=4, help_text="最低价")
    HPrice = models.DecimalField(max_digits=8, decimal_places=4, help_text="最高价")
    CPrice = models.DecimalField(max_digits=8, decimal_places=4, help_text="收盘价")

    def __str__(self):
        return f"{self.symbol} - {self.datatime}"
