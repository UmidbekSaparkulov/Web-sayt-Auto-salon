from django.shortcuts import render
from .models import About, Sections
from collection.models import Collection 
from contact.models import Contact_info
from blog.models import Blog, Category
def aboutView(request):
    about = About.objects.first()
    collection = Collection.objects.all().order_by('-id')[:6]
    section = Sections.objects.all()
    category = Category.objects.all()
    contactme = Contact_info.objects.all()
    blog = Blog.objects.all().order_by('-id')
    cat = request.GET.get('cat')
    if cat:
        blog = blog.filter(category__title__iexact=cat)
    context = {
        'abouts': about,
        'sections' : section,
        'blogs': blog,
        'categories': category,
        'contactme': contactme,
        'collections': collection,
    }
    return render(request, 'about.html', context)
