from rest_framework import serializers
from core.models import Retsept
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'telefon_raqami', 'tugijlgan_sana']

        extra_kwargs = {
            'password': {
                'write_only': True,
            },
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class RetseptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retsept
        fields = ['id', 'sarlavha', 'masalliqlar', 'pishirish_vaqti', 'qiyinlik_darajasi', 'egasi']
        read_only_fields = ['id', 'egasi']