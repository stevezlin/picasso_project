from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth

from .models import CreatePost

class PostForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)


class NewUserForm(forms.Form):
    username = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()


def homepage(request):
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request
        form = NewUserForm(request.POST)

        if form.is_valid():
            # Create a new user object populated with the data we are
            # giving it from the cleaned_data form
            user = User.objects.create(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email'],
            )

            # As soon as our new user is created, we make this user be
            # instantly "logged in"
            auth.login(request, user)
            return redirect('/')

    else:
        # if a GET we'll create a blank form
        form = NewUserForm()

    context = {
        'form': form,
    }
    return render(request, 'pages/home.html', context)


def all_users(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'pages/user_list.html', context)



def user_feed(request, username):
    user = User.objects.get(username=username)

    if request.method == 'POST':

        # Create a form instance and populate it with data from the request
        form = PostForm(request.POST)

        if form.is_valid():
            # Create a new WallPost object populated with the data we are
            # giving it from the cleaned_data form

            CreatePost.objects.create(
                username=username, # Create using the current username
                text=form.cleaned_data['text'],
            )

            # This will just redirect to the current page
            return redirect(request.get_full_path())

    else:
        # if a GET we'll create a blank form
        form = PostForm()

    # We need to get all the posts for this user's username
    posts = CreatePost.objects.filter(username=username)

    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'username': username,
        'form': form,
        'posts': posts,
    }
    return render(request, 'pages/feed.html', context)




def delete_post(request, post_id):
    # Fetch the right WallPost with the post_id, then delete it.
    post = CreatePost.objects.get(id=post_id)
    post.delete()

    # Cool trick to redirect to the previous page
    return redirect(request.META.get('HTTP_REFERER', '/'))




def update_post(request, post_id):
    new_text = request.POST['text']

    # Load post and then update with new_text
    post = CreatePost.objects.get(id=post_id)
    post.text = new_text
    post.save()

    # Cool trick to redirect to the previous page
    return redirect(request.META.get('HTTP_REFERER', '/'))

