from django import forms
from .serializer import file_serializer
import ipdb
from .models import Handle_cnab


class UploadFileForm(forms.Form):
    file = forms.FileField()
instance = Handle_cnab

# Tratamento da data (yyyy-mm-dd)
def handleData (string):
    ano = string[0:4]
    mes = string[4:6]
    dia = string[6:8]
    print (ano +"-"+ mes +"-"+dia)
    return(ano +"-"+ mes +"-"+dia)

# Tratamento de hora (hh:mm:ss)
def handleHora (string):
    h = string[0:2]
    m = string[2:4]
    s = string[4:6]
    return(h +":"+ m +":"+s)

#Em uma refatoração eu criaria 
# uma Model para os tipo de operações, contendo seu ID de código, nome e Tipo,
#  com uma relação 1:1 com as transações.
def handleTypeOp (string):
    if string == "1":
        return "Débito(+)"
    if string == "2":
        return "Boleto(-)"
    if string == "3":
        return "Financiamento(-)"
    if string == "4":
        return "Crédito(+)"
    if string == "5":
        return "Recebimento Empréstimo(+)"
    if string == "6":
        return "Vendas(+)"
    if string == "7":
        return "Recebimento TED(+)"
    if string == "8":
        return "Recebimento DOC(+)"
    if string == "9":
        return "Alguel(-)"
    ...

def handle_uploaded_file(f):
    for chunk in f.chunks():
        #Separação das linhas do documento;
        arrLines = (chunk.decode().splitlines())

        for line in arrLines:
        #Leitura e tratação dos dados;
            tipo = handleTypeOp(line[0])
            data = handleData(line[1:9])
            valor = (int((line[9:18]))/100)
            cpf = (line[19:30])
            cartao = (line[30:42])
            hora = handleHora(line[42:48])
            dono_da_loja = (line[48:62])
            nome_da_loja = (line[62:])
            data= {
                 "type_operations": tipo,
                 "data": data,
                 "valor": valor,
                 "cpf": cpf, 
                 "cartao": cartao,
                 "hora": hora,
                 "dono_da_loja": dono_da_loja.strip(),
                 "nome_da_loja": nome_da_loja.strip()}
            instance.objects.create(**data)

            
    