from django.contrib import admin

# Register your models here.
from .models import Productl,Contact,Orders,orderUpdate

admin.site.register(Productl)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(orderUpdate)