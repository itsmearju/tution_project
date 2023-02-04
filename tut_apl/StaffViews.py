from django.shortcuts import render, redirect


def staff_home(request):
    return render(request, "staff_template/staff_home_template.html")