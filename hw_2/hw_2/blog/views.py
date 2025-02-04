from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import Article

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'listblog.html', {'articles': articles})

def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'detalblog.html', {'article': article})
# Create your views here.
