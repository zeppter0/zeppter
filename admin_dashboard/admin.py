from django.contrib import admin

# Register your models here.
from admin_dashboard.models import Book
from admin_dashboard.models import Category

admin.site.register([Book,Category])
