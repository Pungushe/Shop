from django.db import models

class Record(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.CharField(max_length=255, verbose_name='Email')
    country= models.CharField(max_length=255, verbose_name="Страна")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    city= models.CharField(max_length=255, verbose_name="Город")
    province = models.CharField(max_length=255, verbose_name="Область")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
    def __str__(self):
        return self.first_name + " " + self.last_name