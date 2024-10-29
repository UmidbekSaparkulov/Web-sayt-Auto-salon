from django.shortcuts import render
from blog.models import Blog, Category
from .models import Service
from contact.models import Contact_info
from collection.models import Collection
from about.models import About
def serviceview(request):
    about = About.objects.first()
    service = Service.objects.all()
    contactme = Contact_info.objects.all()
    collection = Collection.objects.all().order_by('-id')[:6]
    category = Category.objects.all()
    blog = Blog.objects.all().order_by('-id')
    cat = request.GET.get('cat')
    if cat:
        blog = blog.filter(category__title__iexact=cat)
    context = {
        'abouts': about,
        'me': contactme,
        'blogs': blog,
        'categories': category,
        'collections': collection,
        'services': service,
    }
    return render(request, 'services.html', context) 