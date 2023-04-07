from django.forms import ModelForm
from resturantapp.models import *

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        labels = {
            'book_name': 'Name',
            'book_email': 'Email',
            'book_phone': 'Phone No.',
            'book_date': 'Date',
            'book_time': 'Time',
            'people': 'No. of People',
            'description': 'description',
        }

class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields =  '__all__'
        labels = {
            'item_name': 'Item Name',
            'category': 'Category of Item',
            'des_price': 'Price of Item',
        }

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        labels = {
            'contact_name': 'Name',
            'contact_email': 'Email',
            'contact_number': 'Phone No.',
            'contact_subject': 'Subject',
            'contact_message': 'Message',
        }
