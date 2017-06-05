from django.shortcuts import render

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
