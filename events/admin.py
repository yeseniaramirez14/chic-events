from django.contrib import admin

from events.models import Event, Description, Contact, BookRequest


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    pass

class DescriptionAdmin(admin.ModelAdmin):
    pass

class ContactAdmin(admin.ModelAdmin):
    pass

class BookRequestAdmin(admin.ModelAdmin):
    pass


admin.site.register(Event, EventAdmin)
admin.site.register(Description, DescriptionAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(BookRequest, BookRequestAdmin)
