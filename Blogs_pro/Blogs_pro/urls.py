"""Blogs_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from Blog_apps import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.postlist_view),
    path('', views.PostListview.as_view()),
    path('tags/<slug:tag_slug>/', views.TagListview.as_view(),name='post_list_by_tag_name'),
    #re_path(r'^post/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',views.post_detail,name='post_detail'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    re_path(r'^(?P<id>\d+)/share/$', views.mail_send_view),

]
#<h3>{{ object.comment_count }} Comment {{ object.comment_count|pluralize }}</h3>

