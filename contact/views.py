from django.shortcuts import render, redirect
from .models import Contact_info
from .forms import ContactForm
from about.models import About


def contactview(request):
    about = About.objects.all()
    contact_info = Contact_info.objects.all()
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('.')

    context = {
        'about': about,
        'form': form,
        'me': contact_info,
    }
    return render(request, 'contact.html', context)
