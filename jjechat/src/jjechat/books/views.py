# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404, render

from jjechat.books.models import Publisher

from jjechat.books.forms import PublisherForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def index(request):
    publisher_list = Publisher.objects.all()
    return render_to_response('books/index.html', {'publisher_list': publisher_list})

def delete(request, id):
    publisher = get_object_or_404(Publisher, id=id)
    publisher.delete()
    return HttpResponseRedirect(reverse("index"))

def add(request):
    if request.method=="POST":
        form = PublisherForm(request.POST)
        if form.is_valid():
            publisher=form.save()
            publisher.save()
            return HttpResponseRedirect(reverse("index"))
    return render(request, 'books/edit.html', {'form': PublisherForm()})
     

def edit(request, id):
    publisher = get_object_or_404(Publisher, id=id)
    if request.method == 'POST':
        appForm = PublisherForm(request.POST, instance = publisher)
        if appForm.is_valid():
            publisher = appForm.save();
            publisher.save()
            return HttpResponseRedirect(reverse("index"))
            
    #return render_to_response('books/edit.html', {'form': PublisherForm(instance = publisher)}, context_instance=RequestContext(request))
    return render(request, 'books/edit.html', {'form': PublisherForm(instance = publisher)})