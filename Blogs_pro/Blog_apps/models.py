from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.

class Post(models.Model):
    STATUS_choice=(('draft','DRAFT'),('published','Published'))
    title=models.CharField(max_length=50)
    slug=models.SlugField(max_length=200, unique_for_date='publish')
    author=models.ForeignKey(User,related_name='blog_post', on_delete=models.CASCADE,)
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True) # datetime for create action
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_choice,default='draft')
    tags=TaggableManager()
    class Meta:
        ordering=('-publish',)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail',
                       args=[self.slug])
    @property
    def comment_count(self):
        return Comments.objects.filter(active=True).count()

    # def get_absolute_url(self):
    #     return reverse('post_detail',
    #                    args=[self.publish.year,
    #                          self.publish.strftime('%m'),
    #                          self.publish.strftime('%d'),
    #                          self.slug])


    # model releted to comment section
class Comments(models.Model):
    post = models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE,)
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=60)
    body=models.TextField()
    created = models.DateTimeField(auto_now_add=True)  # datetime for create action
    updated = models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    class Meta:
        ordering=('-created',)
    def __str__(self):
        return 'commented by {} on {} '.format(self.name,self.post)

