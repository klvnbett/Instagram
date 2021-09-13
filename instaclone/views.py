from django.shortcuts import render,redirect
from django .http import Http404,HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
# from .forms import *
from django.db.models import F

# Create your views here.
def index(request):
    return render(request,'instapp/index.html')
