from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def index_page(request):
   return  render(request , "website/index.html")

def about_page(request):
   return render(request , "website/about.html")

def contact_page(request):
   return render(request , "website/contact.html")

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