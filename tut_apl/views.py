from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import auth
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from tut_apl.EmailBackEnd import EmailBackEnd
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from tut_apl.models import CustomUser,  Courses,  SessionYearModel
from .forms import RegStudentForm

# Create your views here.

def about(request):
    return render(request,'abc.html')

def homepage(request):
    return render(request,'home.html')

def loginPage(request):
    return render(request, 'login.html')

def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        if user != None:
            login(request,user)
            user_type = user.user_type

            if user_type == '1':
                return redirect('admin_home')
                
            elif user_type == '2':
                # return HttpResponse("Staff Login")
                return redirect('staff_home')
                
            elif user_type == '3':
                # return HttpResponse("Student Login")
                return redirect('student_home')
            else:
                messages.error(request, "Invalid Login!")
                return redirect('login')
        else:
            messages.error(request, "Invalid Login Credentials!")
            #return HttpResponseRedirect("/")
            return redirect('login')


def student(request):
    courses = Courses.objects.all()
    forms = RegStudentForm()
    context = {
        "courses": courses,
        "forms": forms,
    }
    return render(request,'student_signup.html',context)


def reg_student_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('student')
    else:
        form = RegStudentForm(request.POST, request.FILES)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            con_password = form.cleaned_data['confirm_password']
            address = form.cleaned_data['address']
            session_year_id = form.cleaned_data['session_year_id']
            course_id = form.cleaned_data['course_id']
            gender = form.cleaned_data['gender']
            phone = form.cleaned_data['phone']
            
            # Getting Profile Pic first
            # First Check whether the file is selected or not
            # Upload only if file is selected
            if len(request.FILES) != 0:
                profile_pic = request.FILES['profile_pic']
                fs = FileSystemStorage()
                filename = fs.save(profile_pic.name, profile_pic)
                profile_pic_url = fs.url(filename)
            else:
                profile_pic_url = None
            

            if password == con_password:
                
                    try:
                        user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=3)
                        user.students.address = address

                        course_obj = Courses.objects.get(id=course_id)
                        user.students.course_id = course_obj

                        session_year_obj = SessionYearModel.objects.get(id=session_year_id)
                        user.students.session_year_id = session_year_obj

                        user.students.gender = gender
                        user.students.phone = phone
                        user.students.profile_pic = profile_pic_url
                        user.save()

                        # subject = 'ABC TUTIONS'
                        # message = 'Congrats, You have successfully registered with us and your login password is: ' + password
                        # recipient = form.cleaned_data.get('email')     #  recipient =request.POST["inputTagName"]
                        # send_mail(subject, 
                        # message, settings.EMAIL_HOST_USER, [recipient])

                        messages.success(request, "Successfully Registered!")
                        return redirect('student')

                    except: 
                           
                           messages.error(request, "Registration Failed!")
                           return redirect('student')
            else:
                messages.error(request, "password do not match!")
                return redirect('student')        
        
        else:
            messages.error(request, "form not valid!")
            return redirect('student')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')
