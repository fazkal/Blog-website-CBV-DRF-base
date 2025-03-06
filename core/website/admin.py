from django.contrib import admin
from website.models import contact,newsletter

# Register your models here.
class websiteAdmin(admin.ModelAdmin):
    date_hierarchy='created_date'
    list_display=('name','subject','created_date')
    list_filter=('email',)
    ordering=['created_date']
    search_fields=('name','subject','message')
admin.site.register(contact ,websiteAdmin)
admin.site.register(newsletter)
