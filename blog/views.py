from django.shortcuts import render
from .models import Post

# Create your views here.

def vista(request):
	list_article=Post.objects.all()
	return render(request,'blog/articulos.html', {'list_article':list_article})