from django import template
from django.db.models import Count
from Blog_apps.models import Post
register=template.Library()

@register.simple_tag(name='my_tag')
def total_posts():
    return Post.objects.count()

@register.inclusion_tag("Blog_apps/latest_post.html")
def show_latest_post():
    latest_post=Post.objects.order_by('-publish')[:4]
    return {'latest_post':latest_post}

@register.simple_tag
def get_most_commented_posts(count=4):

    return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]





