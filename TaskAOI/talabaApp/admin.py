from django.contrib import admin
from django.contrib.auth import models
from homiy.models import Homiy
# Register your models here.
from .models import Student,TalabaHomiy



class HomiyInline(admin.TabularInline):
    model = TalabaHomiy
    readonly_fields = ('ajratilgan_suma','student')
    extra = 1

class StudentAdmin(admin.ModelAdmin):
    list_display = ['fish', 'phone', 'OTM', 'type', 'talaba_hommiyi', 'contract_price']
    list_filter = ['type', 'OTM']
    search_fields = ['OTM', 'type', 'fish', 'phone']
    list_per_page = 15
    inlines = [HomiyInline]

admin.site.register(Student,StudentAdmin)
admin.site.register(TalabaHomiy)