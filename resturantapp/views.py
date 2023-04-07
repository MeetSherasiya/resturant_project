from django.shortcuts import render, redirect
from resturantapp.models import Menu, Book, Contact
from django.contrib import messages
from datetime import date
from twilio.rest import Client
# Create your views here.

today = date.today()
def index(request):

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        time = request.POST.get("time")
        people = request.POST.get("people")
        desc = request.POST.get("message")

        if date < str(today):
            messages.warning(request,"Please Enter a Valid Date")
            return redirect('/')
        if len(name) < 1:
            messages.warning(request,"Please Enter a Valid Name")
            return redirect('/')
        if len(phone) != 10:
            messages.warning(request,"Please Enter a Valid Phone Number")
            return redirect('/')
        
        myquery = Book(book_name=name,book_email=email,book_phone=phone,book_date=date,book_time=time,people=people,description=desc)
        myquery.save()
        messages.success(request,"We will Send the message on your phone number.")

        # Twilio for sent message to user your booking is conformed

        # client = Client("AC7a61ac7176e0a76a9d1f160af8f89822", "64696d1a3eb6d69f7173a6f838dffb4b")
        # client.messages.create(to=("+91" + phone),
        #                             from_ = "+15855581968",
        #                             body = f"Hello {name}, Your Real Taste Resturant Booking is Conformed.\nDate: {date}\nTime: {time}\nPeople: {people}\n\nHave a grate day {name}"
        #                                 )
        return render(request,"index.html")

    allItems = []
    catItem = Menu.objects.values('category','id')
    categ = {item['category'] for item in catItem}
    for cat in categ:
        item = Menu.objects.filter(category=cat)
        allItems.append([item,cat])

    params = {'allItems':allItems}
    return render(request,'index.html',params)


def contact(request):
    if request.method == "POST":
        contact_name = request.POST.get("contactname")
        contact_email = request.POST.get("contactemail")
        contact_number = request.POST.get("contactnumber")
        contact_subject = request.POST.get("contactsubject")
        contact_message = request.POST.get("contactmessage")

        myquery = Contact(contact_name=contact_name,contact_email=contact_email,contact_number=contact_number,contact_subject=contact_subject,contact_message=contact_message)
        myquery.save()
        messages.success(request,"Your Message Send Successfullly.")
        return render(request,"contact.html")

    return render(request,"contact.html")


