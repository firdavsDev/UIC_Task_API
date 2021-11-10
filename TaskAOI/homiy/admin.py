from django.contrib import admin
from .models import Homiy
from talabaApp.models import Student
# Register your models here.
class StudentInline(admin.TabularInline):
    model = Student
    # readonly_fields = ('user','shaxs', 'fish', 'phone', 'price', 'group_name')
    extra = 1

class HomiyAdmin(admin.ModelAdmin):
    list_display = ['fish', 'phone', 'shaxs', 'price', 'group_name']
    list_filter = ['shaxs', 'price']
    search_fields = ['fish', 'shaxs', 'price', 'group_name']
    list_per_page = 20
    inlines = [StudentInline]

admin.site.register(Homiy)