from django.contrib import admin
from .models import Doctor_form,Doctor_class

# Register your models here.

admin.site.register([Doctor_class,Doctor_form])