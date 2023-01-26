from .models import HandleCnab
from rest_framework import serializers
import ipdb

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = HandleCnab
        fields = '__all__'
        # read_only_fields = [
        #         "typeOperations",
        #         "data",
        #         "valor",
        #         "cpf",
        #         "cartao",
        #         "hora",
        #         "donoDaLoja",
        #         "nomeDaLoja"
        #     ]
    
    def create(self, validated_data):
        ipdb.set_trace()
        HandleCnab.objects.create(data=validated_data)
        return 
