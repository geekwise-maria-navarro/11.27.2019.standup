from bank2.models import Branch
from rest_framework import serializers



class Branch_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Branch
        fields = [
            'branch_name',
            'branch_location'
        ]