from bank2.models import Branch, Customer
from rest_framework import serializers



class Branch_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Branch
        fields = [
            'branch_name',
            'branch_location'
        ]

class Customer_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'customer_name',
            'customer_email'
        ]