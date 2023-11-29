from app1.models import Usuarios
from app1 import serializers

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Usuarios
        fields = ['nombres', 'apellidos', 'celular', 'email', 'direccion', 'contrasena', 'is_active']

    def validate_nombres(self, value):
        if len(value) < 3:
            raise serializers.ValidationError({'nombres': 'Los nombres deben tener al menos 3 caracteres'})

    def validate_apellidos(self, value):
        if len(value) < 3:
            raise serializers.ValidationError({'apellidos': 'Los apellidos deben tener al menos 3 caracteres'})

    def validate_email(self, value):
        if not value.endswith('@example.com'):
            raise serializers.ValidationError({'email': 'El correo electrónico debe terminar con @example.com'})

    def validate_contrasena(self, value):
        if len(value) < 8:
            raise serializers.ValidationError({'contrasena': 'La contraseña debe tener al menos 8 caracteres'})
