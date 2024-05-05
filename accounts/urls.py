from django.urls import path
from accounts.views.customer import *
from accounts.views.user import *
urlpatterns = [
    path('login', UserLoginAPIView.as_view(), name='login'),
    path('list-customer', GetCustomerListAPIView.as_view(), name='list-customer'),
    path('create-customer', CreateCustomerAPIView.as_view(), name='create-customer'),
    path('extract-details', ExtractDataFromAttachedFile.as_view(), name='extract-details'),
]