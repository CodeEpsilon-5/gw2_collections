from django.contrib import admin
from markdownx.admin import AdminMarkdownxWidget
from .models import Build


# Register your models here.

admin.site.register(Build)

