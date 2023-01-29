from .models import Handle_cnab
from rest_framework import serializers
import ipdb

class file_serializer(serializers.ModelSerializer):
    class Meta:
        model = Handle_cnab
        fields = [
                 "type_operations",
                 "data",
                 "valor",
                 "cpf",
                 "cartao",
                 "hora",
                 "dono_da_loja",
                 "nome_da_loja"
             ]



    
class return_serializer(serializers.ModelSerializer):
    class Meta:
        model = Handle_cnab
        fields = [
                 "type_operations",
                 "data",
                 "valor",
                 "cpf",
                 "cartao",
                 "hora",
                 "dono_da_loja",
                 "nome_da_loja",
                 "saldo_da_loja"
             ]

    saldo_da_loja = serializers.SerializerMethodField()
    def get_saldo_da_loja(self, obj: Handle_cnab):
        saldo = 0
        acc = 0
        
        loja = Handle_cnab.objects.filter(nome_da_loja = obj.nome_da_loja)    
         #Pegar todas transaçoes de uma mesma loja
         # condicional verificando o [-2] do tipo da operação
         # soma ou sub => acSaldo
         
        for trans in loja:
             if trans.type_operations[-2] == "-":
                 acc = trans.valor
                 saldo += -acc
             if trans.type_operations[-2] == "+":
                 acc = +trans.valor
                 saldo += +acc
        return saldo
