from django import forms
from .serializer import FileSerializer
from .models import HandleCnab


class UploadFileForm(forms.Form):
    file = forms.FileField()



def handle_uploaded_file(f):
    ...