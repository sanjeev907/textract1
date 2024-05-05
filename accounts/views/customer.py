from accounts.models.customer import Customer
from accounts.serializers.customer import CustomerSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from utils.common.utils import extract_data_from_file
import json
from accounts.models.customer_doc import CustomerDocument

class GetCustomerListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    pagination_classes = PageNumberPagination
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CreateCustomerAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        serializer = CustomerSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
            
        except Exception as e:
            return Response(str(e), {'error':'Error creating customer'})
        


class ExtractDataFromAttachedFile(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        attached_file = request.FILES.get('file')
        
        if not attached_file:
            return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Extract data from the attached file
        extracted_data = extract_data_from_file(attached_file)
        
        if not extracted_data:
            return Response({"error": "Failed to extract data from the file"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create a Customer object
        customer_data = {
            "first_name": extracted_data.get("first_name"),
            "surname": extracted_data.get("surname"),
            "nationality": extracted_data.get("nationality"),
            "created_by": request.user.id  # Assuming user is authenticated and request.user is available
        }
        print(customer_data)
        
        customer_serializer = CustomerSerializer(data=customer_data)
        
        if customer_serializer.is_valid():
            customer = customer_serializer.save()
            
            # Create a CustomerDocument object
            customer_document = CustomerDocument.objects.create(
                customer=customer,
                attached_file=attached_file,
                extracted_json=json.dumps(extracted_data)
            )
            
            return Response({"success": "Customer created successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)