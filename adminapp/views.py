from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from resturantapp.models import *
from .forms import *
from django.urls import reverse

# Create your views here.

for e in User.objects.all():
    adminuser = (e.username).capitalize()

def login(request):
    try:
        if request.user.is_authenticated:
            return redirect('/admin/dashboard')

        if request.method == "POST":
            username = request.POST['username']
            userpassword = request.POST['pass']
            myuser = User.objects.filter(username = username)
            if not myuser.exists():
                messages.info(request,"Invalid Credentials")
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            myuser = authenticate (username = username, password=userpassword)

            if myuser and myuser.is_superuser:
                login(myuser)
                return redirect('/admin/dashboard')

            messages.info(request, 'Invalid password')
            return redirect('/admin/')
    
        return render(request,'login.html')
    
    except Exception as e:
        print(e)

def logout_admin(request):
    logout(request)
    return render(request,'login.html')

def dashboard(request):
    objs = Book.objects.order_by("book_date")
    context = {'objs':objs, 'adminuser':adminuser}
    return render(request, 'dashboard.html', context)

def createBook(request):
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin/dashboard')

    context = {'form':form, 'adminuser':adminuser}
    return render(request,'create_book.html', context)

def updateBook(request, pk):
    book = Book.objects.get(id=pk)
    form = BookForm(instance=book)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('/admin/dashboard')
    
    context = {'form':form, 'adminuser':adminuser}
    return render(request,'update_book.html', context)


def deleteBook(request,pk):
    book = Book.objects.get(id=pk)
    if request.method == "POST":
        book.delete()
        return redirect('/admin/dashboard')

    # context = {'obj': book, 'adminuser':adminuser}
    return HttpResponseRedirect(reverse('dashboard'))
    # return render(request,'delete.html', context)



def menu(request):
    objs = Menu.objects.all()
    context = {'objs':objs, 'adminuser':adminuser}
    return render(request, 'menu.html', context)

def createMenu(request):
    form = MenuForm()
    if request.method == "POST":
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/admin/menu')

    context = {'form':form, 'adminuser':adminuser}
    return render(request,'create_menu.html', context)


def updateMenu(request, pk):
    book = Menu.objects.get(id=pk)
    form = MenuForm(instance=book)

    if request.method == "POST":
        form = MenuForm(request.POST, request.FILES ,instance=book)
        if form.is_valid():
            form.save()
            return redirect('/admin/menu')
    
    context = {'form':form, 'adminuser':adminuser}
    return render(request,'update_menu.html', context)


def deleteMenu(request,pk):
    book = Menu.objects.get(id=pk)
    if request.method == "POST":
        book.delete()
        return redirect('/admin/menu')
    
    return HttpResponseRedirect(reverse('menu'))


def contact(request):
    objs = Contact.objects.all()
    context = {'objs':objs, 'adminuser':adminuser}
    return render(request, 'admin_contact.html', context)

def updateContact(request, pk):
    book = Contact.objects.get(id=pk)
    form = ContactForm(instance=book)

    if request.method == "POST":
        form = ContactForm(request.POST ,instance=book)
        if form.is_valid():
            form.save()
            return redirect('/admin/contact')
    
    context = {'form':form, 'adminuser':adminuser}
    return render(request,'update_contact.html', context)


def deleteContact(request,pk):
    book = Contact.objects.get(id=pk)
    if request.method == "POST":
        book.delete()
        return redirect('/admin/contact')

    return HttpResponseRedirect(reverse('contact'))