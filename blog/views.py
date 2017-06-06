import glob
import os

from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from MySite.settings import MEDIA_ROOT
from blog.models import Post


def home(request):
    template_name = 'blog/home.html'
    posts = Post.objects.all()

    for i in posts:
        i.content = i.content[0:100] + "....."

    context = {'object_list': posts}
    return render(request, template_name, context)


def details(request, postn):
    template_name = 'blog/details.html'
    post = Post.objects.get(id=postn)

    context = {'post': post}
    return render(request, template_name, context)


def post(request):
    if request.method == 'POST':
            title = request.POST['title']
            content = request.POST['content']
            img = request.FILES['img']

            posts = Post.objects.all()
            flag = True

            # Prevent repetitive imaged
            for i in glob.glob(MEDIA_ROOT + "\\blog_img\\*"):
                if i.split("\\")[-1] == img.name:
                    os.remove(i)
                    break

            # Prevent repetitive posts
            for i in posts:
                if i.title == title:
                    flag = False

            if flag:
                new_post = Post(title=title, user=User.objects.get(username=request.user.username), content=content, img=img, is_published=True)
                new_post.save()

            return redirect("home")
    else:
        return render(request, 'blog/add_post.html', {})
