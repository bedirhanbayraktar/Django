from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from blog.models import Blog, Category



def index(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    context = {
        "blogs": Blog.objects.filter(is_active=True, is_home=True),
        "categories": Category.objects.all()
    }
    return render(request, "blog/index.html", context)

def blogs(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    context = {
        "blogs": Blog.objects.filter(is_active=True),
        "categories": Category.objects.all()
    }
    return render(request, "blog/blogs.html", context)

def blog_details(request, slug):
    if not request.user.is_authenticated:
        return redirect("login")
    
    blog = Blog.objects.get(slug=slug)

    return render(request, "blog/blog-details.html", {
        "blog": blog
    })
    
def blogs_by_category(request, slug):
    if not request.user.is_authenticated:
        return redirect("login")
    
    context = {
        "blogs": Category.objects.get(slug=slug).blog_set.filter(is_active=True),
        "categories": Category.objects.all(),
        "selected_category": slug
    }
    return render(request, "blog/blogs.html", context)