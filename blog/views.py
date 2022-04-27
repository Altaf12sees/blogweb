from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Blog
from django.urls import reverse_lazy

from django.views import generic

def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs}
    return render(request, 'blog.html', context)

def blog_detail(request, pk):
    blogs = get_object_or_404(Blog, id=pk)
    context = {'blogs':blogs}
    return render(request, 'blog_detail.html', context)

#using generic listview
class BlogListView(generic.ListView):
    template_name = 'blog.html'
    context_object_name = 'blogs'
    def get_queryset(self):
        blogs = Blog.objects.all()
        return blogs

#using generic detailview
class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    context_object_name = 'blogs' 

#create view
class CreateBlogView(generic.CreateView):
    model = Blog
    template_name = 'add_blog.html'
    fields = ['title', 'details']

class UpdateBlogView(generic.UpdateView):
    model = Blog
    template_name = 'add_blog.html'
    fields = ['title', 'details']

#delete view
class DeleteBlogView(generic.DeleteView):
    model = Blog
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('blog')