from django.contrib import admin
from django.urls import path,include
#auth
from django.contrib.auth import views as auth_views
from users import views as user_view
from homiy.views import addAriza
from django.views.generic import TemplateView

from django.conf.urls import url
from django.contrib.auth import views

urlpatterns = [
    path('admin/login/', auth_views.LoginView.as_view(template_name='users/admin.html'), name='login'), #Custom admin
    path('admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    
    #Login Register Logout 
    path('rigester/',user_view.rigester,name='rigester'), 
    path('login/',auth_views.LoginView.as_view(template_name = 'users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'users/logout.html'),name='logout'),
    #home
    path('',addAriza,name='home'),
    path('sendAdmin/', TemplateView.as_view(template_name="sendAdmin.html"),name='sendAdmin'),
    #API
    path('api/', include('api.urls')),
]
