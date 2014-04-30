from django.contrib import admin

from .models import Invitation, Person

class PersonInline(admin.TabularInline):
    model = Person
    extra = 0

class InvitationAdmin(admin.ModelAdmin):
    list_display = ('name', 'guests', 'responded')
    readonly_fields = ('responded',)
    inlines = (PersonInline,)

admin.site.register(Invitation, InvitationAdmin)
