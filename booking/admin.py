from django.contrib import admin
from .models import Booking

#--- Настройка админ панели для страницы booking
class BookingAdmin(admin.ModelAdmin):
	list_display = ('user','service','datetime')
	fields = ('user','service','datetime')

	'''
	def show_datetime(self, obj):
		book = Booking.objects.all()
		booklist = []
		for item in book:
			booklist.append(item.datetime_id)

		result = Booking.objects.exclude(id__in=booklist)
		return result
	'''
admin.site.register(Booking, BookingAdmin)
