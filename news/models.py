from django.db import models


class CurrencyRate(models.Model):
    currency_code = models.CharField(max_length=10, verbose_name="Код валюты")
    rate = models.DecimalField(max_digits=10, decimal_places=4, verbose_name="Курс")
    date = models.DateField(verbose_name="Дата")
    change_percent = models.FloatField(default=0.0, verbose_name="Изменение in %")

    def __str__(self):
        return f"{self.currency_code} — {self.rate} ({self.date})"


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name="Наименование")
    content = models.TextField(blank=True, verbose_name="Контент")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name="Фото")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at', 'title']
