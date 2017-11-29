from django.db import models
from datetime import datetime
# Create your models here.
from nsepy.commons import StrDate
dd_mmm_yyyy = StrDate.default_format(format="%d-%b-%Y")

class Stock(models.Model):
    symbol=models.CharField(default='NA',primary_key=True,max_length=200)
    def __str__(self):
        return self.symbol

class Share(models.Model):
    symbol=models.ForeignKey(Stock,db_index=True)
    series=models.CharField(default='NA',max_length=200)
    date = models.DateTimeField(default=datetime.now())
    prev_close=models.FloatField(default=0.0)
    open=models.FloatField(default=0.0)
    high = models.FloatField(default=0.0)
    low = models.FloatField(default=0.0)
    last = models.FloatField(default=0.0)
    close=models.FloatField(default=0.0)
    vwap=models.FloatField(default=0.0)
    volume = models.IntegerField(default=0)
    turnover=models.FloatField(default=0.0)
    trades = models.IntegerField(default=0)
    deliverable_volume=models.IntegerField(default=0)
    percentage_deliverable=models.FloatField(default=0.0)
    def __str__(self):
        return self.symbol