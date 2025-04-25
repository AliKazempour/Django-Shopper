from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'phone_number', 'photo')
    search_fields = ('user__username', 'phone_number')


admin.site.register(UserProfile,UserProfileAdmin)