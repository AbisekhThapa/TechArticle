from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from django.views.generic import ListView

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles })

def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', { 'article': article })

class CatListView(ListView):
    template_name = 'articles/category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat' : self.kwargs['category'],
            'articles' : Article.objects.filter(category__name=self.kwargs['category'])
        }
        return content
