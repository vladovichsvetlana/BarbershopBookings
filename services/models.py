from django.db import models

#creating model Services
class Services(models.Model):
    service = models.TextField() 
    about = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.service
