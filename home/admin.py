from django.contrib import admin
from home.models import Contact



# Register your models here.
admin.site.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_submitted')
    list_filter = ('date_submitted',)
    search_fields = ('name', 'email')