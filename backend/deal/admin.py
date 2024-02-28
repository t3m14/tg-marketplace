from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.models import User as us
from feed.models import *

admin.site.unregister(Group)
admin.site.unregister(us)

admin.site.register(Chapter)
admin.site.register(Category)
admin.site.register(Subcategory)

admin.site.register(Service)
admin.site.register(Order)

