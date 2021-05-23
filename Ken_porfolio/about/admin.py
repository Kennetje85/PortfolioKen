from about.models import About
from django.contrib import admin


class AboutAdmin(admin.ModelAdmin):
    pass

admin.site.register(About, AboutAdmin)

from django.contrib import admin

# Register your models here.
