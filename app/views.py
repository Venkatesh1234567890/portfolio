from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.filter(active=True, featured=True)[0:3]
    context = {'posts': posts}
    return render(request, 'base/index.html', context)

def posts(request):
    posts = Post.objects.filter(active=True)
    context = {'posts': posts}
    return render(request, 'base/posts.html', context)

def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {'post': post}
    return render(request, 'base/post.html', context)

def profile(request):
    return render(request, 'base/profile.html')



# CRUD VIEWS
@login_required(login_url="home")
def createpost(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('posts')
    context = {'form':form}
    return render(request, 'base/post_form.html',context)



@login_required(login_url="home")
def updatepost(request,slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES,instance=post)
        if form.is_valid():
            form.save()
        return redirect('posts')
    
    context = {'form':form}
    return render(request, 'base/post_form.html',context)

@login_required(login_url="home")
def deletepost(request,slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        post.delete()
        return redirect('posts')
    
    context = { 'items': post}
    return render(request, 'base/delete.html',context)



def sendEmail(request):
    if request.method == 'POST':
        # You might want to validate the form data using Django forms here.

        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        template = render_to_string('base/email_template.html', {'name': name, 'email': email, 'message': message})

        subject = request.POST.get('subject', 'Default Subject')  # Provide a default subject if not present

        email = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            ['venkatesh18121@gmail.com']
        )

        email.fail_silently = False
        email.send()

        return render(request,'base/email_sent.html')
