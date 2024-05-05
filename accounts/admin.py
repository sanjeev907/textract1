from django.contrib import admin
from accounts.models.country import Country 
from accounts.models.user import User
from accounts.models.document_set import DocumentSet
from accounts.models.customer import Customer
from accounts.models.customer_doc import CustomerDocument

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'country_name',)
    search_fields = ('email',)


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class DocumentSetAdmin(admin.ModelAdmin):
    list_display = ('document_name','has_backside', 'ocr_labels',)
    search_fields = ('country',)
    ordering = ('document_name',)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'surname', 'nationality', 'sex', )
    ordering = ('first_name', 'surname',)
    search_fields = ('nationality',)


class CustomerDocumentAdmin(admin.ModelAdmin):
    list_display = ('customer', 'created_at',)


admin.site.register(User, UserAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(DocumentSet, DocumentSetAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(CustomerDocument, CustomerDocumentAdmin)