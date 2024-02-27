from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Scripts
# Create your views here.
@login_required(login_url='loginUser')
def homePage(request):
    script = Scripts.objects.all()
    return render(request,'homePage.html',{'script':script})