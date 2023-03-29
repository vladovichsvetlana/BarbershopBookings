from django.db import models
from usermodify.models import UserModify
from services.models import Services
from timesforbooking.models import TimesForBooking

#creating a model Booking
class Booking(models.Model):
    user = models.ForeignKey(UserModify, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    datetime = models.ForeignKey(TimesForBooking, on_delete=models.CASCADE)
    dateday = models.DateField(default='2023-01-01') #booking date

    def __str__(self):
        return self.service.service
