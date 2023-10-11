from django.contrib import admin
from .models import advertisement
from django.db import models

#'created_at','created_date'
class advertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description','price','created_at','update_at','auction','created_date']
    list_filter = ['auction','created_at']
    auction = ['make_auction_as_false']
    fieldsets = (
        ('Общее',{
            'fields': ('title', 'description')
        }),
        ('Финансы',{
            'fields':('price','auction'),
            'classes': ['collapse']
        })
    )

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_true(self,request,queryset):
        queryset.update(auction=False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

admin.site.register(advertisement,advertisementAdmin)