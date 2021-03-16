from django.shortcuts import render,get_object_or_404
from django.views import generic
from .models import Post,Comments
from django.core.mail import send_mail
from Blog_apps.forms import EmailsendForm,commentform
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from taggit.models import Tag

# Create your views here with FBV.
# def postlist_view(request):
#     post_list=Post.objects.all()
#     paginator=Paginator(post_list,3)
#     page_number=request.GET.get('page')
#     try:
#         post_list=paginator.page(page_number)
#     except PageNotAnInteger:
#         post_list=paginator.page(1)
#     except EmptyPage:
#         post_list=paginator.page(paginator.num_pages)
#     return render(request,'Blog_apps/list.html',{'post_list':post_list})

class PostListview(generic.ListView,):
    model = Post
    template_name = 'Blog_apps/list.html'
    paginate_by = 2
class TagListview(generic.ListView,):
    model = Post
    template_name = 'Blog_apps/list.html'
    paginate_by = 2

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get('tag_slug'))




class PostDetail(generic.DetailView,):
    model = Post
    template_name = 'Blog_apps/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comments.objects.filter(post=self.get_object()).order_by('-created')
        if self.request.user.is_authenticated:
            context['comment_form'] = commentform(instance=self.request.user)

        return context

    def post(self, request, *args, **kwargs):
        new_comment = Comments(name=request.POST.get('name'),
                               email=request.POST.get('email'),
                               body=request.POST.get('body'),
                               post=self.get_object())
        new_comment.save()
        return self.get(self, request, *args, **kwargs)









#####333mail send view-----#######33
def mail_send_view(request,id):
    post=get_object_or_404(Post,id=id,status='published')
    sent=False
    if request.method=='POST':
        form = EmailsendForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            post_url=request.build_absolute_uri(post.get_absolute_url())

            #subject = '''{} recommneds you to read {} '''.format((cd['name'],post.title))
            subject = '{} recommends you to read {} '.format(cd['name'], post.title,)
            message='Read Post at : \n {}\n\n{}\'comments:\n{}'.format(post_url,cd['name'],cd['comments'])

            send_mail(subject,message,'Durga@durgasoft.com',[cd['to']])
            sent=True
    else:
        form=EmailsendForm()
    return render(request,'Blog_apps/sharebymail.html',{'form':form,'post':post,'sent':sent})