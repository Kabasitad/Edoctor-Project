from django.contrib import admin

# Register your models here.
from .models import Checkin , Medicine , OrderLoan

admin.site.register(Checkin)
admin.site.register(Medicine)
admin.site.register(OrderLoan)


