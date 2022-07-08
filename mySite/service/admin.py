from django.contrib import admin
from .models import Service
from .models import Contact

# Register your models here.

admin.site.register(Service)
admin.site.register(Contact)