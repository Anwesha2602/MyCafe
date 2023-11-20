from django.contrib import admin
from .models import Logger
from .models import Menu_items
admin.site.register(Menu_items)
admin.site.register(Logger) 
# Register your models here.
