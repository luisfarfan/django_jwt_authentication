from rest_framework import serializers

from user.models import User, Products


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, required=False, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'last_name', 'username', 'password', 'products')

    def create(self, validated_data):
        validated_data.pop('products')
        if 'products' in validated_data:
            pass

        user = User.objects.create(**validated_data)
        return user
