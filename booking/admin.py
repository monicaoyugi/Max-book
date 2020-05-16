from django.contrib import admin
from booking.models import Movie, Tickets, Seats

# Register your models here.
admin.site.register(Movie)
admin.site.register(Tickets)
admin.site.register(Seats)
