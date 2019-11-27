from bank2.models import Branch, Customer
from rest_framework import viewsets
from bank2.serializer import Branch_Serializer, Customer_Serializer


class Branch_Viewsets(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Branch.objects.all()
    serializer_class = Branch_Serializer

class Customer_Viewsets(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class = Customer_Serializer