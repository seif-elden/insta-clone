from django.contrib import admin
from .models import photo , more_user_info ,follow , comments
# Register your models here.

admin.site.register(photo)
admin.site.register(more_user_info)
admin.site.register(follow)
admin.site.register(comments)
