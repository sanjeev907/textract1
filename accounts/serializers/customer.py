from rest_framework.serializers import ModelSerializer
from accounts.models.customer import Customer
from accounts.models.document_set import DocumentSet


class DocumentSetViewSerializer(ModelSerializer):
    class Meta:
        model = DocumentSet
        fields = '__all__'


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ('surname', 'first_name', 'nationality', 'sex', 'created_by', )