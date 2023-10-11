from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone

class advertisement(models.Model):
    title = models.CharField('заголовок', max_length=255)
    description = models.TextField('описание')
    price = models.DecimalField('цена',max_digits=10, decimal_places=2)
    auction = models.BooleanField('торг', help_text='Отметьте,если торг уместен')
    created_at = models.DateTimeField('дата',auto_now_add=True)
    update_at = models.DateTimeField('обновлённая дата',auto_now=True)


    @admin.display(description='дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M%:%S")
            return format_html(
        '<span style="color: green; font=weight: bold;">Сегодня в {}</span>',created_time
            )
        return self.created_at.strftime("%d-%m-%Y %H:%M:%S")

    class Meta:
        db_table = 'advertisement'

    def __str__(self):
        return f'<advertisement: advertisement(id={self.id}, title={self.title}, price={self.price:.2f})>'
