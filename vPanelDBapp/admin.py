from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import HUGOgene, Panel, Subpanel, User, PermissionGroup, LogChanges


admin.site.register(Panel)
admin.site.register(HUGOgene)
admin.site.register(Subpanel)
admin.site.register(PermissionGroup)
admin.site.register(LogChanges)


class MyUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = User


class MyUserCreationForm(UserCreationForm):

    permissiongroup = forms.ModelChoiceField(queryset=PermissionGroup.objects.all())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('permissiongroup',)


class MyUserAdmin(UserAdmin):

    form = MyUserChangeForm
    add_form = MyUserCreationForm
    fieldsets = UserAdmin.fieldsets + (
        ('Personal info', {'fields': ('permissiongroup',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'password1',
                       'password2', 'permissiongroup')}
         ),
    )

admin.site.register(User, MyUserAdmin)