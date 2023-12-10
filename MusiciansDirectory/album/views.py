from django.shortcuts import render,redirect
from . import forms
from . import models

# Create your views here.
def index(request):
    if request.method == "POST":
        postform = forms.AlbumForm(request.POST)
        if postform.is_valid():
            postform.save()
            return redirect('index')
    else:
        postform =  forms.AlbumForm()
    return render(request,'index.html' ,{"data":postform})

def edit_album(request,id):
    post = models.AlbumModel.objects.get(pk=id)
    postform = forms.AlbumForm(instance=post)
    if request.method == "POST":
        postform = forms.AlbumForm(request.POST , instance=post)
        if postform.is_valid():
            postform.save()
            return redirect('homepage')
    return render(request,'index.html' ,{"data":postform})

def delete_model(request,id):
    postform = models.AlbumModel.objects.get(pk=id)
    postform.delete()
    return redirect("homepage")