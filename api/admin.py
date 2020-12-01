from django.contrib import admin
from api.models import Digit

# Register your models here.

class DigitAdmin(admin.ModelAdmin):

    list_display = ["id", "classification"]

admin.site.register(Digit, DigitAdmin)
