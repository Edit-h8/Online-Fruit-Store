from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from .forms import Contact_Form
from django.contrib import messages
# Create your views here.

def index_page(request):
   return  render(request , "website/index.html")

def about_page(request):
   return render(request , "website/about.html")

def contact_page(request):

   if request.method == "POST":

      form = Contact_Form(request.POST)

      if form.is_valid():
         form.save()
         messages.success(request,"Your Mesaage Successfuly Send")
         return redirect('website:index')
      else:
         messages.error(request , "CAPTCHA or Anythong Isn't True !!")
         

   contact = {"form" : Contact_Form() }
   return render(request , "website/contact.html" , contact)

@login_required
def profile(request):
   return render(request , "website/profile.html")


@login_required
def change_info(request):
   if request.method == "POST":
      username = request.POST.get("username")
      request.user.username = username
      request.user.save()
      messages.success(request, "Username changed successfully.")
      return redirect("website:profile")

   return render(request, "account/change_info.html")