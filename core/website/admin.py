from django.contrib import admin

from django.contrib import admin
from website.models import Contact,Newsletter

# # Register your models here.
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    list_display = ('name','subject','email','message',)
    list_filter =['name',]
    ordering = ['created_date']
    search_fields = ['Name','Subject','email','message']

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email',)

admin.site.register(Contact,ContactAdmin)
admin.site.register(Newsletter,NewsletterAdmin)

