from django.db import models
#импорт стороннего шаблона для формы ввода номера телефона. Незнаю зачем я его добавил, но наверное так лучше :))
from phone_field import PhoneField
from django.contrib.auth.models import User


#creating models user modify for add user info number phone 
class UserModify(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    phone = PhoneField(blank=True)

    def __str__(self):
        return str(str(self.phone) + ' ' + self.user.username )
