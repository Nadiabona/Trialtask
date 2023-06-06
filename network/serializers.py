from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from network.models import Products, Unit


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        read_only_fields = ("id", "created", "updated", "user")
        fields = "__all__"

    def get_queryset(self):
        return Products.objects.filter(is_deleted=False)

class UnitSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    # def get_queryset(self):
    #     return Unit.objects.filter(is_deleted=False)

    # def validate(self,attrs: dict) -> dict:
    #     if attrs['level'] ==0 and attrs['amount_due_in_kopeeks'] !=0:
    #         raise ValidationError("Amount due should be zero")
    #     elif attrs['level'] !=0 and (attrs['level']-attrs['supplier'])!=1:
    #         raise ValidationError("The level of supplier is not correct")
    #     return attrs

    class Meta:
        model = Unit
        read_only_fields = ("id", "created", "updated", "user")
        fields = "__all__"
