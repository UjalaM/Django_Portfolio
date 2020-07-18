from django.contrib import admin

# Register your models here.
from contact.models import ContactForm

class ContactFormAdmin(admin.ModelAdmin):
    search_fields = ['pk','name']
    list_filter = ['name']
    list_display = ['pk','created_at','name','contact_num','email_id','message']
    
admin.site.register(ContactForm, ContactFormAdmin)