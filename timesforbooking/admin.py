from django.contrib import admin

from .models import TimesForBooking
from django.conf import settings


class TimesForBookingMod(admin.ModelAdmin):
	list_display = ('get_str_day','dtime')

	def get_str_day(self, obj):
		for i in settings.DAYS:
			if str(i[0]) == str(obj.day):
				return str(i[1])
	get_str_day.short_description = "Day"
admin.site.register(TimesForBooking, TimesForBookingMod)