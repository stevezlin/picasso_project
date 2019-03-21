from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth

# Uploadcare
from .models import CreatePost
from .models import UploadImage
from .forms import PostForm

class NewUserForm(forms.Form):
    username = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']



def homepage(request):
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request
        form = NewUserForm(request.POST)

        if form.is_valid():
            # Create a new user object using the ModelForm's built-in .save()
            # giving it from the cleaned_data form.
            user = User.objects.create(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email'],
            )   
               
            # As soon as our new user is created, we make this user be
            # instantly "logged in".
            auth.login(request, user)
            return redirect('/')

    else:
        # if a GET we'll create a blank form
        form = NewUserForm()

    context = {
        'form': form,
    }
    return render(request, 'pages/home.html', context)



#Lists all users
def all_users(request):
    users = User.objects.order_by('date_joined')
    context = {
        'users': users,
    }
    return render(request, 'pages/user_list.html', context)



def user_feed(request, username):
    users = User.objects.all()
    context = {

    }
    
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = PostForm()

    try:
        posts = UploadImage.objects.all()
    except UploadImage.DoesNotExist:
        posts = None

    return render(request, 'pages/feed.html', {'posts': posts, 'form': form})


def delete_post(request, post_id):
    # Fetch the right WallPost with the post_id, then delete it.
    post = UploadImage.objects.get(id=post_id)
    post.delete()

    # Cool trick to redirect to the previous page
    return redirect(request.META.get('HTTP_REFERER', '/'))
    
    
def like_post(request, post_id):
    # Update the tweet to add the user as a "liker"
    post = UploadImage.objects.get(id=post_id)
    post.liked.add(request.user)
    # tweet.save() # Already adds!

    # Redirect to wherever they came from
    return redirect(request.META.get('HTTP_REFERER', '/'))
    



