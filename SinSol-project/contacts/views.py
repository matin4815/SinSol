from django.shortcuts import render, redirect
from .models import Contact


def contacts(request):
  return render(request, 'contacts/contact.html')


def contact(request):
  if request.method =="POST":
    name = request.POST['name']
    phone = request.POST['phone']
    email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['message']

  contact = Contact(name=name, phone=phone, email=email, 
  subject=subject, message=message)

  contact.save()
   
  return redirect("/contacts/")
