from django.contrib import admin

# Register your models here.
from account.models import FriendRequest

admin.site.register(FriendRequest)