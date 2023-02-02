from django.urls import path
from . import views
from .import AdminViews


urlpatterns = [
path('', views.loginPage, name="login"),
path('admin_home',AdminViews.admin_home, name="admin_home"),
path('add_staff',AdminViews.add_staff, name="add_staff"),
path('add_staff_save',AdminViews.add_staff_save, name="add_staff_save"),
path('tlogin',views.tlogin, name="tlogin"),
]