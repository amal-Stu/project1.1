
from django.http import HttpResponse
from django.template import loader
from .models import Post
def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


from .models import User

def users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})


from .models import Post

def blogs(request):
    blogs = Post.objects.all()
    return render(request, 'blogs.html', {'blogs': blogs})

from django.shortcuts import render, get_object_or_404
from .models import Post

def blogdetails(request, blog_id):
    blog = get_object_or_404(Post, pk=blog_id)
    return render(request, 'blogdetails.html', {'blog': blog})

from .models import Comment
def comments(request):
    comments = Comment.objects.all()
    return render(request, 'comments.html', {'comments': comments})
from django.shortcuts import render
from .models import Category

def categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})
