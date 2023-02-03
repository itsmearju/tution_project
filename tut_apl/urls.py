from django.urls import path
from . import views
from .import AdminViews


urlpatterns = [
path('', views.loginPage, name="login"),
path('tlogin',views.tlogin, name="tlogin"),
path('admin_home',AdminViews.admin_home, name="admin_home"),
path('add_staff',AdminViews.add_staff, name="add_staff"),
path('add_staff_save',AdminViews.add_staff_save, name="add_staff_save"),
path('add_student',AdminViews.add_student, name="add_student"),
path('add_student_save',AdminViews.add_student_save, name="add_student_save"),

]