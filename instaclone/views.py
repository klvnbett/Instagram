from django.shortcuts import render,redirect
from django .http import Http404,HttpResponse,HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request,'instapp/index.html')
