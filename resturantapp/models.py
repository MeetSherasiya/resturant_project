from django.db import models

# Create your models here.

class Menu(models.Model):
    menu_id = models.AutoField
    item_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default="")
    des_price = models.CharField(max_length=50, default="")
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='./menu/',default="")

    def __str__(self):
        return self.item_name

class Book(models.Model):
    book_id = models.AutoField
    book_name = models.CharField(max_length=100)
    book_email = models.EmailField(default="")
    book_phone = models.CharField(max_length=12)
    book_date = models.DateField()
    book_time = models.TimeField()
    people = models.CharField(max_length=3)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.book_name
    
class Contact(models.Model):
    contact_name = models.CharField(max_length=100)
    contact_email = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    contact_subject = models.CharField(max_length=200)
    contact_message = models.CharField(max_length=2000)

    def __str__(self):
        return self.contact_subject,self.contact_number