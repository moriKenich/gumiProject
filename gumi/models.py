from django.db import models




class Category(models.Model):
    title =models.CharField(verbose_name='シリーズ',max_length=20)
    def __str__(self):
        return self.title
    
class Maker(models.Model):
    makername=models.CharField(verbose_name='メーカー',max_length=20)
    def __str__(self):
        return self.makername
    
class Hard(models.Model):
    hardness=models.CharField(verbose_name='硬さ',max_length=20)
    def __str__(self):
        return self.hardness

class Powder(models.Model):
    powderis=models.CharField(verbose_name='パウダー',max_length=20)
    def __str__(self):
        return self.powderis
    
class GumiPost(models.Model):
    
    
    category=models.ForeignKey(
        Category,
        verbose_name='シリーズ',
        on_delete=models.PROTECT
        )
    
    hard=models.ForeignKey(
        Hard,
        verbose_name='硬さ',
        on_delete=models.PROTECT)
    
    maker=models.ForeignKey(
        Maker,
        verbose_name='メーカー',
        on_delete=models.PROTECT)
    
    powder=models.ForeignKey(
        Powder,
        verbose_name='パウダー',
        on_delete=models.PROTECT)
    
    
    title=models.CharField(
       verbose_name='商品名',
       max_length=200)
    
    comment=models.TextField(
        verbose_name='コメント',)
    
    url=models.TextField(
        verbose_name='URL',)
    
    image=models.ImageField(
        verbose_name='イメージ',
        upload_to='photos')
    
    posted_at=models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True)
    
    price=models.IntegerField(
        verbose_name='定価')
    
    weight=models.IntegerField(
        verbose_name='重量')
    
    
    def __str__(self):
        return self.title

