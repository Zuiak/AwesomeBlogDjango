from django.shortcuts import render
from .models import Article


# Create your views here.
def blog(request):
    posts = Article.objects
    return render(request, 'blog/blog.html', {'article': posts})
