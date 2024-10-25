from django import template
from blog.models import Post
from blog.models import Category
from blog.models import Comment


register = template.Library()

@register .inclusion_tag('blog/blog-popularposts.html')
def latestposts():
    posts = Post.objects.filter(status=True).order_by('published_date')[:4]
    return {'posts': posts}

#-----------------------------------------------------------------------------#

@register .inclusion_tag('blog/blog-postcatgories.html')
def postcategories():
    posts = Post.objects.filter(status=True)
    categories = Category.objects.all()
    cat_dict={}
    for name in categories:
        cat_dict [name] = posts.filter(category=name).count()
    return {'categories': cat_dict}
#-----------------------------------------------------------------------------#
@register .simple_tag(name='comments_count')
def countcomment(pid):
    return Comment.objects.filter(post=pid,approved=True).count()
