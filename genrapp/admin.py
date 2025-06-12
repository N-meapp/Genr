from django.contrib import admin
from .models import *
from genrapp.models import JobApplication,ContactForm
from django.utils.html import format_html


# Register your models here.


admin.site.register(Our_Products)
admin.site.register(Gallery)
admin.site.register(Offer)
admin.site.register(Enquiry)
admin.site.register(Career)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'job_position', 'view_cv')

    def view_cv(self, obj):
        if obj.cv:
            return format_html('<a href="{}" target="_blank">Download CV</a>', obj.cv.url)
        return "No file uploaded"
    
    view_cv.short_description = "CV"

admin.site.register(JobApplication, JobApplicationAdmin)
# admin.site.register(ContactForm)
admin.site.register(News)
admin.site.register(Login)
admin.site.register(Count)
admin.site.register(WorkPlace)
admin.site.register(CustomerReview)
admin.site.register(Solarpanel)
admin.site.register(Invertor)
admin.site.register(Invoice)
admin.site.register(Package)
admin.site.register(Product)
admin.site.register(Brand)




class Additional_imagesTabular(admin.TabularInline):
    model = Addiotional_work_images

class WorkAdmin(admin.ModelAdmin):
    inlines = [Additional_imagesTabular]

admin.site.register(Our_Works, WorkAdmin)

admin.site.site_header = "GEN-R"

@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'enquiry_type', 'submitted_at')
    search_fields = ('name', 'email', 'enquiry_type')
    list_filter = ('enquiry_type', 'submitted_at')