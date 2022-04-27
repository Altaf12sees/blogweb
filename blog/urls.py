from django.urls import path
from . import views

urlpatterns = [
    #function based view
    # path('', views.blog, name='blog'),
    # path('blog_detail/<int:pk>', views.blog_detail, name='blog_detail'),

    #class based view
    path('', views.BlogListView.as_view(), name="blog"),
    path('blog_detail/<int:pk>', views.BlogDetailView.as_view(), name='blog_detail'),
    path('create_blog/', views.CreateBlogView.as_view(), name="create_blog"),
    path('update_blog/<int:pk>', views.UpdateBlogView.as_view(), name="update_blog"),
    path('<pk>/delete_blog', views.DeleteBlogView.as_view(), name="delete_blog"),
]