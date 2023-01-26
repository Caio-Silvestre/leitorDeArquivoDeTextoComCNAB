from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm, handle_uploaded_file
from rest_framework.views import APIView, Request, Response, status
from rest_framework import generics
from .serializer import FileSerializer
from .models import HandleCnab
import ipdb
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('success/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

class successViews(APIView):
    ...

    