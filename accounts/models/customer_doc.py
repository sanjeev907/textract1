from django.db import models
from accounts.models.customer import Customer


class CustomerDocument(models.Model):
    customer = models.ForeignKey(Customer, on_delete= models.CASCADE)
    attached_file = models.FileField(blank=True, null=True, upload_to='media/attached_file')
    extracted_json = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)