
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from blog.models import BlogUser,BlogGroup,UserManager
from blog.models import Post,PostType,Comment,Category,Attached

from blog.forms import UserCreationForm,UserChangeForm
from blog.forms import PostCreationForm
# Register your models here.

class BlogUserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm
    
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('UserName', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('UserName', 'password')}),
        ('Personal info', {'fields': ('Email',)}),
        ('Permissions', {'fields': ('is_admin','Groups',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('UserName', 'Email', 'password1', 'password2')}
        ),
    )
    search_fields = ('UserName',)
    ordering = ('UserName',)
    filter_horizontal = ()
    

admin.site.register(BlogUser,BlogUserAdmin)
admin.site.register(BlogGroup)
admin.site.register(Post)
admin.site.register(PostType)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Attached)

