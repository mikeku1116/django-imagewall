from django.shortcuts import render, redirect
from .forms import UploadModelForm


def index(request):

    form = UploadModelForm()

    if request.method == "POST":
        form = UploadModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/photos')

    context = {
        'form': form
    }

    return render(request, 'photos/index.html', context)
