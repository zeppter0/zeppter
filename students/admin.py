from django.contrib import admin
from teacher.models import School,Subject
# Register your models here.

admin.site.register([School,Subject])
