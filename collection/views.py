from django.shortcuts import render
from collection.models import Collection

def collectionview(request):
    collection = Collection.objects.all().order_by('-id')[:5]
    context = {
        'collections': collection,
    }
    return render(request, 'collection.html', context)
