from django.shortcuts import render,redirect
from . import forms
from . import models

# Create your views here.
def show(request):
    if request.method == "POST":
        postform = forms.MusicianForm(request.POST)
        if postform.is_valid():
            postform.save()
            return redirect('show')
    else:
        postform = forms.MusicianForm()
    return render(request, 'show.html',{'form':postform})

def edit_musician(request,id):
    post = models.Musician.objects.get(pk=id)
    postform = forms.MusicianForm(instance=post)
    if request.method == "POST":
        postform = forms.MusicianForm(request.POST,instance=post)
        if postform.is_valid():
            postform.save()
            return redirect('show')
    
    return render(request, 'show.html',{'form':postform})