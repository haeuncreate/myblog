from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

def home(request):
  blogs = Blog.objects
  return render(request, 'home.html', {'blogs':blogs})

def detail(request, blog_id):
  blog_detail = get_object_or_404(Blog, pk = blog_id)
  return render(request, 'detail.html', {'blog_detail':blog_detail})

def new(request):  # new.html 을 띄우는 함수
  return render(request, 'new.html')

def create(request):  # 입력받은 내용을 데이터베이스에 넣어주는 함수
  blog = Blog()
  blog.title = request.GET['title']
  blog.body = request.GET['body']
  blog.pub_date = timezone.datetime.now()
  blog.save() # 객체.delete()
  return redirect('/blog/'+str(blog.id))

  # redirect 함수와 render 함수의 차이
  # redirect('https://google.com')
