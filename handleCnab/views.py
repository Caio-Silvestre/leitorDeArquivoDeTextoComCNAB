from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm, handle_uploaded_file
from rest_framework.views import APIView, Request, Response, status
from rest_framework import generics
from .serializer import file_serializer, return_serializer
from .models import Handle_cnab
from django.forms.models import model_to_dict
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

class successDetailsViews(APIView):
    def get (self,request:Request, nome_l):
        cnab = Handle_cnab.objects.filter(nome_da_loja = nome_l).all()
        serializer = return_serializer(cnab, many=True)
        return Response(serializer.data)

class successViews(APIView):     
    def get (self,request:Request):
        # Pega o nome no canab => cnab[0].dono_da_loja
      
        serializer = return_serializer(Handle_cnab.objects.all(), many=True)

        # Pega o nome no serializer.data => serializer.data[0]["dono_da_loja"]
        lista = sorted(serializer.data, key=lambda k: k["nome_da_loja"])
        def saldo_total():
            saldo = 0
            acc = 0

            for trans in lista:
                if trans["type_operations"][-2] == "-":
                    acc = float(trans["valor"])
                    saldo += (acc*-1)
                if trans["type_operations"][-2] == "+":
                    acc = float(trans["valor"])
                    saldo += acc
            if saldo < 0:
                return saldo*-1
            return saldo
        saldo_total()
        return Response({"transações": serializer.data, "lucro_total_do_banco": saldo_total()})


        