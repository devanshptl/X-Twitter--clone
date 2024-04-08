from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    talks = Talks.objects.all().order_by("-created_at")
    context= {'talks':talks}
    return render(request,'home.html',context)

def people(request):
    if request.user.is_authenticated:
	    list = Profile.objects.all()
	    return render(request, 'people.html', {"list":list})
    else:
    	messages.warning(request, ("You Must Be Logged In To View This Page..."))
    	return redirect('home')

def search(request):
	if request.method == "POST":
		search = request.POST['search']
		searched = User.objects.filter(username__contains = search)
		return render(request, 'search.html', {'search':search, 'searched':searched})
	else:
		return render(request, 'search.html', {})

def profile(request,pk):
    if request.user.is_authenticated: 
        try:
            profile_page = Profile.objects.get(user_id = pk)
            # profile_page = get_object_or_404(Profile, user_id = pk)
            talks = Talks.objects.filter(user_id = pk).order_by("-created_at")
            context = {'profile_page' : profile_page ,'talks':talks}    
            return render(request,'profile.html',context)

        except Profile.DoesNotExist:
            return HttpResponse('<h1>User does not exist</h1>')
    else:
        messages.warning(request, "You must login first ---")
        return redirect('/')

def createprofile(request):
    if request.user.is_authenticated:
        form = createprofileform(request.POST or None,request.FILES or None)
        if request.method == "POST":
            if form.is_valid():
                create = form.save(commit=False)
                create.user = request.user
                create.save()
                messages.success(request, "Successfully Created")
                return redirect('/') 
        return render(request,'profilepage.html',{'form':form})
    else:
        messages.warning(request, "You must login first ---")
        return redirect('/')


def write(request):
    if request.user.is_authenticated:
        form = Talkform(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                talk = form.save(commit=False)
                talk.user = request.user
                talk.save()
                messages.success(request, "Successfully posted")
                return redirect('/') 
        else:
            return render(request,'talks.html',{'form':form})
    else:
        messages.warning(request, "You must login first ---")
        return redirect('/')
     
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return redirect('/')
    else:
        return render(request,'login.html',{})

def Signup(request):
    form = SignUpForm()
    if request.method == "POST":
        # obj = User.objects.get(id=request.user.id)
        form = SignUpForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('createprofile')
    return render(request,'signup.html',{'form':form})

def update_profile(request):
    if request.user.is_authenticated :
        current = Profile.objects.get(user=request.user)
        form = createprofileform(request.POST or None,request.FILES or None,instance=current)
        if form.is_valid() :
            form.save()
            messages.success(request, 'The post has been created successfully.')
            return redirect('/') 
        return render(request,'update_profile.html',{'form':form})

def logout_user(request):
    logout(request)
    return redirect('home')

def likes(request, pk):
    if request.user.is_authenticated :
        like = Talks.objects.get(user_id = pk)
        if like.likes.filter(id = request.user.id):
            like.likes.remove(request.user)
        else:
            like.likes.add(request.user)
        return redirect(request.META.get("HTTP_REFERER"))
    else:
        messages.warning(request, "To like talks you must login first")
        return redirect('home')
    
def Delete(request, pk):
    if request.user.is_authenticated :
        delete = Talks.objects.get(user_id = pk)
        delete.delete()
        messages.success(request, "Successfully deleted")
        return redirect(request.META.get("HTTP_REFERER"))

def Delete_user(request, pk):
    if request.user.is_authenticated :
        delete = Profile.objects.get(user_id = pk)
        delete.delete()
        messages.success(request, "Successfully deleted")
        return redirect('logout')

def Edit(request,pk):
    if request.user.is_authenticated :
        edit = Talks.objects.get(user_id = pk)
        form = Talkform(request.POST or None,instance=edit)
        if request.method =="POST":
            if form.is_valid() :
                form.save()
            # form2.save()
                messages.success(request, 'Talk successfully edited ') 
                return redirect('/')
        else:
            return render(request,'talks.html',{'form':form})

