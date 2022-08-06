from django.contrib import admin
from home.models import Contact
from home.models import Search
from home.models import Booking

# Register your models here.
admin.site.register(Contact)
admin.site.register(Search)
admin.site.register(Booking)