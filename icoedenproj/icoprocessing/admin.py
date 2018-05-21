
# Register your models here.
from django.contrib import admin

from .models import ICOModel


@admin.register(ICOModel)
class ICOAdmin(admin.ModelAdmin):
    pass