from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Blog


def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs}
    return render(request, 'blog.html', context)

def blog_detail(request, pk):
    blogs = get_object_or_404(Blog, id=pk)
    context = {'blogs':blogs}
    return render(request, 'blog_detail.html', context)
