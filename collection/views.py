from django.shortcuts import render
from collection.models import Collection
from about.models import About
from blog.models import Blog

def collectionview(request):
    about = About.objects.first()
    blog = Blog.objects.all()
    collection = Collection.objects.all().order_by('-id')[:6]
    context = {
        'collections': collection,
        'blogs': blog,
        'abouts': about,

    }
    return render(request, 'collection.html', context)
