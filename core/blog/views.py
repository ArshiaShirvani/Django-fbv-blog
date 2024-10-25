from django.shortcuts import render

from django.shortcuts import render , get_list_or_404
from blog.models import Post,Comment
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from blog.forms import CommentForm
from django.contrib.auth.decorators import login_required



def homeblog(request,**kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name')!=None:
        posts = Post.objects.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_name')!=None:
        posts=Post.objects.filter(author__username=kwargs['author_name'])
    if kwargs.get('tag_name')!=None:
        posts=posts.filter(tags__name__in=[kwargs['tag_name']])
    posts=Paginator(posts,5)
    try:
        page_number=request.GET.get('page')
        posts=posts.get_page(page_number)
    except PageNotAnInteger:
        posts=posts.get_page(1)
    except EmptyPage:
        posts=posts.get_page(1)
    context = {'posts': posts}
    return render(request,'blog/blog-home.html',context)

def singleblog(request,pid):
    if request.method == 'POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            form.save()
    form=CommentForm()
    post = get_list_or_404(Post,id=pid,status=1)
    post = Post.objects.get(id=pid,status=1)
    comments=Comment.objects.filter(approved=True,post=post.id)
    context = {'post':post,'comments':comments}
    return render(request,'blog/blog-single.html',context)

def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method =='GET':
        if s:=request.GET.get('s'):
            posts=posts.filter(content__contains=s)
    context = {'posts': posts}
    return render(request,'blog/blog-home.html',context)
