from django.shortcuts import render
from about.models import About
from collection.models import Collection
def blogView(request):
    about = About.objects.all()
    collection = Collection.objects.all().order_by('-id')[:5]

    context = {
        'abouts': about,
        'collections': collection,
    }
    return render(request, 'blog.html', context)


def indexView(request):
    return render(request, 'index.html')

