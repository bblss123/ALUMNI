from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Tie)
admin.site.register(Activity)
admin.site.register(City)
admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Department)
admin.site.register(Reply)
admin.site.register(Industry)