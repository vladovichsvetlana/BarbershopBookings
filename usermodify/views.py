from django.http import HttpResponseRedirect
from usermodify.forms import RegisterUserForm
from usermodify.forms import LoginUserForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from usermodify.models import UserModify
from booking.models import Booking
from services.models import Services
from timesforbooking.models import TimesForBooking
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from usermodify.utils import DataMixin
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.models import User

import time
import datetime

#------- form index
def index(request):
	services = Services.objects.all()[:20]
	return render(
		request,
		'index.html',
		{
			'services': services
		})
#---- generating a register page  ---- 
class RegisterUser(DataMixin, CreateView):
	form_class = RegisterUserForm
	template_name = 'login/register.html'
	success_url = reverse_lazy('login')

	def get_context_data(self,*,object_list=None, **kwards):
		context = super().get_context_data(**kwards)
		c_def = self.get_user_context(title="Registration")
		return dict(list(context.items()) + list(c_def.items()))

#---- generating a login page ---- 
class LoginUser(DataMixin, LoginView):
	form_class = LoginUserForm
	template_name = 'login/login.html'
	success_url = reverse_lazy('/')

	def get_context_data(self,*,object_list=None, **kwards):
		context = super().get_context_data(**kwards)
		c_def = self.get_user_context(title="Autorization")
		return dict(list(context.items()) + list(c_def.items()))
	def get_success_url(self):
		return reverse_lazy('backoffice')

# redirect for logout
def logout_view(request):
    logout(request)
    return redirect('login')

 
#--------------   for autorisation users  ----------------------

from django.contrib.auth.decorators import login_required
#redirect for non-logged in users
@login_required(login_url='/login')

# page index backofice
def backoffice(request):
	weekDay = time.strftime("%w", time.localtime())
	services = Services.objects.all()[:20]
	book = Booking.objects.all()
	booklist = []
	for item in book:
		booklist.append(item.datetime_id)
	# время из базы на сегодняшний день
	timesToday = TimesForBooking.objects.all().filter(dtime__gte = time.strftime("%H:%M:%S", time.localtime())).filter(day=weekDay)
	# фильтр времен по уже забранированным
	timesToday = timesToday.exclude(id__in=booklist)
	timesTomorrow = []
	i = int(weekDay) 
	today = datetime.date.today()
	#cycle to generate days after today
	for j in range(0,6):
		timeTomorrow = {
			'day': '',
			'query': [],
			'dayForPost': '' #to substitute the date attribute and send back the dates in the format required for the database 
		}
		tomorrow = today + datetime.timedelta(days=(j+1))
		timeTomorrow['day'] = tomorrow.strftime("%d.%m.%y")
		timeTomorrow['dayForPost'] = tomorrow.strftime("%Y-%m-%d")
		timeTomorrow['query'] = TimesForBooking.objects.all().filter(day = str(i+1 if i != 6 else 0)).exclude(id__in=booklist)
		timesTomorrow.append(timeTomorrow)
		i = i+1 if i != 6 else 0
	
	return render(
		request,
		'backoffice/index.html',
		{
			#sending data to the client
			'today': today.strftime("%d.%m.%y"),
			'todayBaseFormat':today.strftime("%Y-%m-%d"),
			'services': services,
			'timesToday': timesToday,
			'timesTomorrow': timesTomorrow,
			'weekDay': weekDay,

		})

# page index backofice as superuser
def backofficeAsAdmin(request):
	weekDay = time.strftime("%w", time.localtime())
	services = Services.objects.all()[:20]
	allusers = User.objects.all()
	book = Booking.objects.all()
	booklist = []
	for item in book:
		booklist.append(item.datetime_id)
	# время из базы на сегодняшний день
	timesToday = TimesForBooking.objects.all().filter(dtime__gte = time.strftime("%H:%M:%S", time.localtime())).filter(day=weekDay)
	# фильтр времен по уже забранированным
	timesToday = timesToday.exclude(id__in=booklist)
	timesTomorrow = []
	i = int(weekDay) 
	today = datetime.date.today()
	#cycle to generate days after today
	for j in range(0,6):
		timeTomorrow = {
			'day': '',
			'query': [],
			'dayForPost': '' #to substitute the date attribute and send back the dates in the format required for the database 
		}
		tomorrow = today + datetime.timedelta(days=(j+1))
		timeTomorrow['day'] = tomorrow.strftime("%d.%m.%y")
		timeTomorrow['dayForPost'] = tomorrow.strftime("%Y-%m-%d")
		timeTomorrow['query'] = TimesForBooking.objects.all().filter(day = str(i+1 if i != 6 else 0)).exclude(id__in=booklist)
		timesTomorrow.append(timeTomorrow)
		i = i+1 if i != 6 else 0
	
	return render(
		request,
		'backoffice/admin.html',
		{
			#sending data to the client
			'today': today.strftime("%d.%m.%y"),
			'todayBaseFormat':today.strftime("%Y-%m-%d"),
			'services': services,
			'timesToday': timesToday,
			'timesTomorrow': timesTomorrow,
			'weekDay': weekDay,
			'users': allusers,
		})




# post save booking
def postBron(request):
	dTime = request.POST['daytime']
	service = request.POST['service']
	dDate = request.POST['day-date']
	userId = request.user.id
	bron = Booking(datetime_id = dTime, service_id = service, user_id = userId, dateday = dDate)
	bron.save()
	return HttpResponseRedirect("/backoffice/myBooking") #redirect to my bookings

# delete booking
def delBron(request, delid):
	record = Booking.objects.get(id = delid)
	record.delete()
	return HttpResponseRedirect("/backoffice/myBooking") #redirect to my bookings
	


# page my bookings
def myBooking(request):
	book = Booking.objects.all().filter(user_id = request.user.id)
	return render(
		request,
		'backoffice/booking.html',
		{
			'book': book
		})


# post save booking
def postBronAdmin(request):
	dTime = request.POST['daytime']
	service = request.POST['service']
	dDate = request.POST['day-date']
	userId = request.POST['userid']
	bron = Booking(datetime_id = dTime, service_id = service, user_id = userId, dateday = dDate)
	bron.save()
	return HttpResponseRedirect("/backoffice/allBooking") #redirect to my bookings



# page all bookings
def allBooking(request):
	if request.user.is_superuser:
		book = Booking.objects.all()
		return render(
			request,
			'backoffice/allbooking.html',
			{
				'book': book
			})
	else:
		return HttpResponseRedirect("/backoffice/myBooking") #redirect to my bookings