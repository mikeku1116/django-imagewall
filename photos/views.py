from django.shortcuts import render
from .forms import UploadModelForm


def index(request):

    form = UploadModelForm()

    context = {
        'form': form
    }

    return render(request, 'photos/index.html', context)
