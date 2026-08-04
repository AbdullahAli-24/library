from django.contrib import admin
from .models import Book

# تسجيل موديل الكتب عشان يظهر في لوحة التحكم
admin.site.register(Book)
