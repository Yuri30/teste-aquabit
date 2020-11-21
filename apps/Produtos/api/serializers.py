from rest_framework import serializers
from apps.Produtos.models import Produtos, Pratos


class PratosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pratos
        fields = '__all__'


class ProdutosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produtos
        fields = '__all__'


class CascataProdutosSerializer(serializers.ModelSerializer):
    pratos = PratosSerializer(many=True)

    class Meta:
        model = Produtos
        fields = ('id', 'categoria', 'pratos')

    def create(self, validated_data):
        pratos_data = validated_data.pop('produto')
        produtos = Produtos(**validated_data)
        produto.save()
        pratos = Pratos.objects.create(Pratos=produtos, **pratos_data)
        

        pratos.save()
        return produto