from django.contrib import admin
from . models import Departments,Doctors,Booking,Feedback

class BookingAdmin(admin.ModelAdmin):
    list_display=('id','person_name',
                  'person_mobile',
                  'person_email',
                  'doc_name',
                  'booking_date',
                  'booked_on')

admin.site.register(Departments)
admin.site.register(Doctors)
admin.site.register(Booking,BookingAdmin)
admin.site.register(Feedback)
