from django.shortcuts import render, redirect
from .models import Contact_info
from .forms import ContactForm
from about.models import About
from collection.models import Collection


def contactview(request):
    about = About.objects.first()
    collections = Collection.objects.all().order_by('-id')[:6]
    contact_info = Contact_info.objects.all()
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('.')

    context = {
        'abouts': about,
        'collections': collections,
        'form': form,
        'me': contact_info,
    }
    
    return render(request, 'contact.html', context)
