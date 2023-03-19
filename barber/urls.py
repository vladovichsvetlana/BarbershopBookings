from django.contrib import admin
from django.urls import path, include
from usermodify import views
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login', views.LoginUser.as_view(), name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.RegisterUser.as_view(), name='register'),
    
    #admin panel of the user
    path('backoffice',views.backoffice,name='backoffice'),
    path('backoffice/bron',views.postBron, name='post-bron'),
    path('backoffice/delbron/<int:delid>',views.delBron, name='del-bron'),
    path('backoffice/myBooking',views.myBooking, name='my-booking'),
    path('backoffice/allBooking',views.allBooking, name='all-booking'),
    
    #admin panel of the superuser
    path('backoffice/adminbron',views.postBronAdmin, name='post-bron-admin'),
    path('backoffice/admin',views.backofficeAsAdmin,name='backoffice-as-admin'),
]


if settings.DEBUG:
    import debug_toolbar
    import mimetypes
    mimetypes.add_type("application/javascript", ".js", True)
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
