from django.contrib import admin
from .models import Services

#display fields to the admin
class ServicesAdmin(admin.ModelAdmin):
	list_display = ('service','price')


admin.site.register(Services, ServicesAdmin)


