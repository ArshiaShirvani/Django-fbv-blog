from django.urls import path
from . import views

app_name='blog'

urlpatterns = [
    path('',views.homeblog,name='homeblog'),
    path('<int:pid>',views.singleblog,name='singleblog'),
    path('category/<str:cat_name>',views.homeblog,name='category'),
    path('tag/<str:tag_name>',views.homeblog,name='tag'),
    path('author/<str:author_name>',views.homeblog,name='author'),
    path('search/',views.blog_search,name='search'),
]