from django.contrib import admin

# Register your models here.
from dashboard_app.models import Rent, UserProfile
admin.site.register(Rent)
admin.site.register(UserProfile)
