from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Категорії"

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Категорія', verbose_name='Категорія')
    mainimage = models.ImageField(upload_to='Product', verbose_name='Фото')
    name = models.CharField(max_length=64, verbose_name='Назва')
    sort = models.CharField(max_length=64, verbose_name='Сорт', null=True)
    color = models.CharField(max_length=64, verbose_name='Колір', null=True)
    text = models.TextField(max_length=1000, verbose_name='Опис', null=True)
    product_code = models.CharField(max_length=10, verbose_name='Код', null=True)
    price = models.FloatField(verbose_name='Ціна')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created',]

    class Meta:
        verbose_name_plural = "Товар"
