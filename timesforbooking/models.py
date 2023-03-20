from django.db import models
from django.conf import settings

#creating models times for booking
class TimesForBooking(models.Model):
	
	day = models.IntegerField(choices=settings.DAYS, default="1")
	dtime = models.TimeField()

	def __str__(self):
		return str(self.dtime) + " " + self.getDateTimeName()

	#get weekday name by number - settings.DAYS
	def getDateTimeName(self):
		return str(next(x[1] for x in settings.DAYS if str(x[0]) == str(self.day)))
