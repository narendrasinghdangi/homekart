from django.contrib import admin

# Register your models here.
from .models import farmerupdate, market,Contact

admin.site.register(market)
admin.site.register(Contact)
admin.site.register(farmerupdate)