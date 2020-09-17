from django.shortcuts import render,redirect,get_object_or_404
from .forms import BlogForm, CommentForm
from .models import Blog, Comment
from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
# Create your views here.


def main(request):
    blogs = Blog.objects.all()
    return render(request, 'main.html', {'blogs':blogs})

def my_index(request):
    my_blog = Blog.objects.filter(author = request.user)
    return render(request, 'main.html', {'blogs':my_blog})

def intro(request):
    return render(request, "intro.html")

@login_required(login_url = '/login/')
def create(request):
    if request.method =="POST":
        filled_form = BlogForm(request.POST)
        if filled_form.is_valid():
            temp_form = filled_form.save(commit=False)
            temp_form.author = request.user
            temp_form.save()
            return redirect('main')
    blog_form = BlogForm()
    return render(request, 'create.html',{'blog_form' : blog_form})


@login_required(login_url = '/login/')
def detail(request, blog_id):
    my_blog = get_object_or_404(Blog, pk = blog_id)
    comment_form = CommentForm()
    return render (request, 'detail.html', {'my_blog':my_blog, 'comment_form':comment_form})



def delete(request, blog_id):
    my_blog = Blog.objects.get(pk = blog_id)
    if request.user == my_blog.author :
        myblog.delete()
        return redirect('main')

    raise PermissionDenied


def update(request, blog_id):
    my_blog = Blog.objects.get(pk = blog_id)
    blog_form = BlogForm(instance = my_blog)
    if request.method == "POST":
        updated_form = BlogForm(request.POST, instance=my_blog)
        if updated_form.is_valid():
            updated_form.save()
            return redirect('main')

    return render(request, 'create.html', {'blog_form':blog_form})




def create_comment(request, blog_id):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        temp_form = comment_form.save(commit=False)
        temp_form.author = request.user
        temp_form.blog = Blog.objects.get(pk = blog_id)
        temp_form.save()

        return redirect('detail' , blog_id)

def delete_comment (request, blog_id, comment_id):
    my_comment = Comment.objects.get(pk = comment_id)
    if request.user == my_comment.author :
        my_comment.delete()
        return redirect('detail', blog_id)

    else :
        raise PermissionDenied