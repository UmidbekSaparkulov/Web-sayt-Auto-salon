from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from about.models import About
from collection.models import Collection
from contact.models import Contact_info
from .models import Blog, Category, Tag, Comment
from .forms import CommentForm, SubscribeForm


def indexView(request):
    about = About.objects.first()
    category = Category.objects.all()
    blog = Blog.objects.all().order_by('-id')
    cat = request.GET.get('cat')
    if cat:
        blog = blog.filter(category__title__iexact=cat)
    contactme = Contact_info.objects.all()
    collection = Collection.objects.all().order_by('-id')[:6]


    context = {
        'abouts': about,
        'categories': category,
        'me': contactme,
        'collections': collection,
        'blogs': blog,
    }
    return render(request, 'index.html', context)


def blogView(request):
    comments = Comment.objects.first()
    about = About.objects.first()
    contactme = Contact_info.objects.all()
    blog = Blog.objects.all().order_by('-id')
    tag = Tag.objects.all()
    p = Paginator(blog, 3)
    blog = p.get_page(request.GET.get('page'))
    category = Category.objects.all()
    collection = Collection.objects.all().order_by('-id')[:6]
    cat = request.GET.get('cat')
    form = SubscribeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('.')
    if cat:
        blog = blog.filter(category__title__iexact=cat)
    context = {
        'abouts': about,
        'blogs': blog,
        'me': contactme,
        'categories': category,
        'collections': collection,
        'comment': comments,
        'form': form,
        'tags': tag,
    }

    return render(request, 'blog.html', context)

def detailView(request, pk):
    blog1 = Blog.objects.all()
    cat = request.GET.get('cat')
    about = About.objects.first()
    contactme = Contact_info.objects.all()
    category = Collection.objects.all()
    tag = Tag.objects.all()
    blog = Blog.objects.get(id=pk)

    form = CommentForm(request.POST or None)
    if form.is_valid():
        com = form.save(commit=False)
        com.blog = blog
        com.save()

        return redirect('.')

    context = {
        'blog1': blog1,
        'blogs': blog,
        'abouts': about,
        'me': contactme,
        'categories': category,
        'tags': tag,
        'form': form,
    }
    return render(request, 'single.html', context)