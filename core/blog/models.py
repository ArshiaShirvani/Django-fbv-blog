from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager



class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=255)
    content=models.TextField()
    author = models.ForeignKey(User,on_delete = models.SET_NULL,null=True)
    created_date =models.DateField(auto_now_add =True)
    updated_date = models.DateField(auto_now = True)
    published_date = models.DateTimeField()
    status = models.BooleanField()
    counted_view = models.BigIntegerField()
    tags = TaggableManager()
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='blog/',default='blog/default.png')
    class Meta:
        ordering =['-created_date']
    
        
    def __str__(self):
        return " {} - {} ".format(self.title,self.id)
    
    #def snappit(self):
        #return self.content[:100]

    def get_absolute_url(self):
        return reverse('blog:singleblog', kwargs={"pid": self.id})
    

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    email=models.EmailField()
    subject=models.CharField(max_length=255)
    message=models.TextField(max_length=255)
    approved=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

    class Meta:
        ordering =['-created_date']

    def __str__(self):
        return " {} - {} ".format(self.name,self.id)
