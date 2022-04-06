from django.contrib import admin

from events.models import Event, Description, Contact


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    pass

class DescriptionAdmin(admin.ModelAdmin):
    pass

class ContactAdmin(admin.ModelAdmin):
    pass


admin.site.register(Event, EventAdmin)
admin.site.register(Description, DescriptionAdmin)
admin.site.register(Contact, ContactAdmin)
