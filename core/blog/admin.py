from django.contrib import admin
from blog.models import Post,Category,Comment
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = "created_date"
    list_display = ('title','author','created_date','updated_date','status',)
    #fields =['title','author']
    #exclude =['title']
    list_filter =['status']
    ordering = ['created_date']
    search_fields = ['title','content']
    summernote_fields = ('content')


class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    list_display = ('name','subject','post','created_date','updated_date','message','approved')
    #fields =['title','author']
    #exclude =['title']
    list_filter =['post','name','approved']
    ordering = ['created_date']
    search_fields = ['name','post']


admin.site.register(Comment,CommentAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Category)