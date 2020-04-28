from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.

class Printer(models.Model):

    name = models.CharField(max_length=250, verbose_name='Название принтера')
    api_key = models.CharField(max_length=250, unique=True, blank=False, null=False, verbose_name='Ключ доступа к API')
    check_type = models.CharField(max_length=7, choices=, verbose_name='Тип чека')
    point_id = models.IntegerField(verbose_name='Точка привязки принтера')

    def __str__(self):
        return self.name

    class Meta:
    	verbose_name = 'Принтер'
    	verbose_name_plural = 'Принтеры'


class Check(models.Model):

    new = 'new'
    rendered = 'rendered'
    printed = 'printed'
    status = [(new, 'new'),
                (rendered, 'rendered'),
                (printed, 'printed')]

    printer = models.ForeignKey(Printer, on_delete=models.CASCADE, verbose_name='Принтер')
    check_type = models.CharField(max_length=7, choices= verbose_name='Тип чека')
    order = JSONField(verbose_name='Информация о заказе')
    status = models.CharField(max_length=8, choices=status, default=NEW, verbose_name='Статус чека')
    pdf_file = models.FileField(upload_to='pdf/', null=True, blank=True, verbose_name='PDF-файл')

    def __str__(self):
        return f'{self.order["id"]}_{self.type}'

    class Meta:
    	verbose_name = 'Чек'
    	verbose_name_plural = 'Чеки'