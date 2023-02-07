from django.urls import path
from . import views
from .import AdminViews, StaffViews, StudentViews


urlpatterns = [
path('', views.loginPage, name="login"),
path('doLogin',views.doLogin, name="doLogin"),
path('logout_user',views.logout_user, name="logout_user"),

path('admin_home',AdminViews.admin_home, name="admin_home"),
path('manage_staff',AdminViews.manage_staff, name="manage_staff"),
path('add_staff',AdminViews.add_staff, name="add_staff"),
path('add_staff_save',AdminViews.add_staff_save, name="add_staff_save"),
path('edit_staff/<staff_id>/',AdminViews.edit_staff, name="edit_staff"),
path('edit_staff_save',AdminViews.edit_staff_save, name="edit_staff_save"),
path('delete_staff/<staff_id>/',AdminViews.delete_staff, name="delete_staff"),
path('add_student',AdminViews.add_student, name="add_student"),
path('add_student_save',AdminViews.add_student_save, name="add_student_save"),
path('manage_student',AdminViews.manage_student, name="manage_student"),
path('edit_student/<student_id>',AdminViews.edit_student, name="edit_student"),
path('edit_student_save/',AdminViews.edit_student_save, name="edit_student_save"),
path('delete_student/<student_id>/',AdminViews.delete_student, name="delete_student"),

path('staff_home',StaffViews.staff_home, name="staff_home"),

path('student_home',StudentViews.student_home, name="student_home"),
]