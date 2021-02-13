from django.contrib import admin

# Register your models here.
from admin_dashboard.models import Book, Views,Like,DisLike
from admin_dashboard.models import Category

admin.site.register([Book,Category,Views,Like,DisLike])
