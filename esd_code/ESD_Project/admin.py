from django.contrib import admin
from ESD_Project.models import ClubMember, Club, PaymentMethod
# Register your models here.

admin.site.register(Club)
admin.site.register(ClubMember)
admin.site.register(PaymentMethod)
