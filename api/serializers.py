from rest_framework import serializers
from api.models import Acoes


class AcoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acoes
        fields = ('__all__')