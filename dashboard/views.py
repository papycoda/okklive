from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request=request,
                  template_name="dashboard/menu.html",)


def createnewproj(request):
    return render(request=request,
                  template_name="dashboard/menu.html",)