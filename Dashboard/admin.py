from django.contrib import admin
from .models import People,Custodian,Record,Location


admin.site.register(People)
admin.site.register(Custodian)
admin.site.register(Record)
admin.site.register(Location)