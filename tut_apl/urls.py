from django.urls import path
from . import views
from .import AdminViews, StaffViews, StudentViews


urlpatterns = [
path('', views.loginPage, name="login"),
path('doLogin',views.doLogin, name="doLogin"),
path('logout_user',views.logout_user, name="logout_user"),
path('admin_home',AdminViews.admin_home, name="admin_home"),
path('add_staff',AdminViews.add_staff, name="add_staff"),
path('add_staff_save',AdminViews.add_staff_save, name="add_staff_save"),
path('add_student',AdminViews.add_student, name="add_student"),
path('add_student_save',AdminViews.add_student_save, name="add_student_save"),
path('staff_home',StaffViews.staff_home, name="staff_home"),
path('student_home',StudentViews.student_home, name="student_home"),
]