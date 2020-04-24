from django.contrib import admin
from .models import UserBankDetails, User, Session

# Register your models here.
admin.site.register(User)
admin.site.register(UserBankDetails)
admin.site.register(Session)
