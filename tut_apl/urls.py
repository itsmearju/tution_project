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
path('add_course/', AdminViews.add_course, name="add_course"),
path('add_course_save/', AdminViews.add_course_save, name="add_course_save"),
path('manage_course/', AdminViews.manage_course, name="manage_course"),
path('edit_course/<course_id>/', AdminViews.edit_course, name="edit_course"),
path('edit_course_save/', AdminViews.edit_course_save, name="edit_course_save"),
path('delete_course/<course_id>/', AdminViews.delete_course, name="delete_course"),
path('manage_session/', AdminViews.manage_session, name="manage_session"),
path('add_session/', AdminViews.add_session, name="add_session"),
path('add_session_save/', AdminViews.add_session_save, name="add_session_save"),
path('edit_session/<session_id>', AdminViews.edit_session, name="edit_session"),
path('edit_session_save/', AdminViews.edit_session_save, name="edit_session_save"),
path('delete_session/<session_id>/', AdminViews.delete_session, name="delete_session"),
path('add_subject/', AdminViews.add_subject, name="add_subject"),
path('add_subject_save/', AdminViews.add_subject_save, name="add_subject_save"),
path('manage_subject/', AdminViews.manage_subject, name="manage_subject"),
path('edit_subject/<subject_id>/', AdminViews.edit_subject, name="edit_subject"),
path('edit_subject_save/', AdminViews.edit_subject_save, name="edit_subject_save"),
path('delete_subject/<subject_id>/', AdminViews.delete_subject, name="delete_subject"),

path('staff_home',StaffViews.staff_home, name="staff_home"),

path('student_home',StudentViews.student_home, name="student_home"),
]