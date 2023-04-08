from django.contrib import admin
from account.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin):
    
    list_display = ('id','email','Name','Date_Of_Birth','ContactNumber','is_admin')
    list_filter = ('is_admin',)
    
    fieldsets = (
        (None, {'fields': ('email','password')}),
        ('Personal info', {'fields': ('Name','Date_Of_Birth','ContactNumber')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
        
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'Date_Of_Birth','Name','ContactNumber','password1', 'password2'),
        }),
    )
    
    search_fields = ('email','Name')
    ordering = ('email','id','Name')
    filter_horizontal = ()

admin.site.register(User, UserAdmin)