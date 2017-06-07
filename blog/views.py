from http.client import HTTPResponse

from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from blog.models import Post, Comment


def home(request):
    if request.user.is_authenticated:
        template_name = 'blog/home.html'
        posts = Post.objects.filter(is_published=True)

        for i in posts:
            i.content = i.content[0:100] + "....."

        context = {'object_list': posts, 'plen': len(posts)}
        return render(request, template_name, context)
    else:
        return render(request, 'blog/new_home.html', {})


def details(request, postn):
    if request.user.is_authenticated:
        template_name = 'blog/details.html'
        post = Post.objects.get(id=postn)
        context = {'post': post}
        return render(request, template_name, context)
    else:
        return redirect("logout")


def signup(request):
    template_name = 'registration/signup.html'
    error1 = 0
    error2 = 0
    error3 = 0
    if request.method == "POST":
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        uname = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['new_password1']
        pass2 = request.POST['new_password2']

        if len(User.objects.filter(email=email)) != 0:
            error1 = 2
        if len(User.objects.filter(username=uname)) != 0:
            error1 = 3

        if pass1 is None or pass1 == "":
            error2 = 1
        if pass2 is None or pass2 == "":
            error3 = 1
        if pass1 != pass2 and error2 == 0 and error3 == 0:
            error1 = 1
        if error1 == 0 and error2 == 0 and error3 == 0:
            user = User(first_name=fname, last_name=lname, email=email, username=uname)
            user.set_password(pass1)
            user.save()
            return render(request, 'registration/registered.html', {'uname': uname})
    context = {'error1': error1, 'error2': error2, 'error3': error3}
    return render(request, template_name, context)


def post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            title = request.POST['title']
            content = request.POST['content']
            img = request.FILES['img']
            is_pub = request.POST['is_pub']

            posts = Post.objects.all()
            flag = True

            # Prevent repetitive posts
            for i in posts:
                if i.title == title:
                    flag = False

            if flag:
                new_post = Post(title=title, user=User.objects.get(username=request.user.username), content=content, img=img, is_published=is_pub)
                new_post.save()

            return redirect("home")
        else:
            return render(request, 'blog/add_post.html', {})
    else:
        return redirect("logout")


def edit_post(request, pk):
    if request.user.is_authenticated:
        if request.method == 'POST':
            postr = Post.objects.get(id=int(pk))
            if postr.user.username != request.user.username:
                return redirect("home")
            else:
                if 'title' in request.POST:
                    title = request.POST['title']
                else:
                    title = ""

                if 'content' in request.POST:
                    content = request.POST['content']
                else:
                    content = ""

                if 'img' in request.FILES:
                    img = request.FILES['img']
                else:
                    img = postr.img

                is_pub = request.POST['is_pub']

                postr.title = title
                postr.img = img
                postr.content = content
                postr.is_published = is_pub
                postr.save()

            return redirect("details", int(pk))
        else:
            postd = Post.objects.get(id=int(pk))
            context = {'p': postd}
            return render(request, 'blog/edit_post.html', context)
    else:
        return redirect("logout")


def delete_post(request, pk):
    if request.user.is_authenticated:
        if request.method == 'POST':
            poste = Post.objects.get(id=int(pk))
            if poste.user.username != request.user.username:
                return redirect("home")
            else:
                poste.delete()
            return redirect("home")
        else:
            postd = Post.objects.get(id=int(pk))
            context = {'p': postd}
            return render(request, 'blog/delete_post.html', context)
    else:
        return redirect("logout")


def add_comment(request, pk):
    if request.user.is_authenticated:
        if request.method == 'POST':
            comment = Comment(user=User.objects.get(username=request.user.username), post=Post.objects.get(id=int(pk)), comment_text=request.POST['cText'])
            comment.save()
        return redirect("details", int(pk))
    else:
        return redirect("logout")
