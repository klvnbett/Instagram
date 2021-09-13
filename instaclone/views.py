from django.shortcuts import render,redirect
from django .http import Http404,HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.db.models import F

# Create your views here.
def index(request):
    return render(request,'instapp/index.html')

@login_required(login_url='/accounts/login/')
def profile(request):
    images=Image.objects.all()
    current_user = request.user
    following=Following.objects.filter(username=current_user.username).all()
    followingcount=len(following)
    followers=Following.objects.filter(followed=request.user.username).all()
    followercount=len(followers)
    if request.method == 'POST':
        form = FormDetails(request.POST, request.FILES)
        form1 = FormImage(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()

        if form1.is_valid():
            image = form1.save(commit=False)
            image.profile = current_user.profile
            image.save()

        return redirect('profile')

    else:
        form = FormDetails()
        form1 = FormImage()
    
    return render(request, 'instapp/profile.html', {"form":form,"form1":form1,"images":images,"followingcount":followingcount,"followercount":followercount})

@login_required(login_url='/accounts/login/')
def timeline(request):
    users = User.objects.all()
    images = Image.objects.all()
    follows = Following.objects.all()
    comments = Comment.objects.all()
    if request.method=='POST' and 'follow' in request.POST:
        following=Following(username=request.POST.get("follow"),followed=request.user.username)
        following.save()
        return redirect('timeline')
    elif request.method=='POST' and 'comment' in request.POST:
        comment=Comment(comment=request.POST.get("comment"),
                        image=int(request.POST.get("imageed")),
                        username=request.POST.get("user"),
                        count=0)
        comment.save()
        comment.count=F('count')+1
        return redirect('timeline')
    elif request.method=='POST' and 'image' in request.POST:
        posted=request.POST.get("image")
        for image in images:
            if (int(image.id)==int(posted)):
                image.like+=1
                image.save()
        return redirect('timeline')
    else:
        return render(request, 'timeline.html',{"users":users,"follows":follows,"images":images,"comments":comments})
