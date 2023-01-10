import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from ESD_Project.models import ClubMember,Club, PaymentMethod
from ESD_Project.forms import NewMemberForm, ClubForm, PaymentMethodForm

# admin - username : c password : adminpassword
# club rep - username 1JK password: justapassword

# make functions to render web pages

def home(request):
    return render(request, "ESD_Project/home.html")

def about(request):
    return render(request, "ESD_Project/about.html")

def contact(request):
    return render(request, "ESD_Project/contact.html")

## Club
def view_account(request):
    club_details = Club.objects.all()
    return render(request, "ESD_Project/my_account.html",{"club_details":club_details})

def update_account(request,account_id):
    account = Club.objects.get(pk=account_id)
    form = ClubForm(request.POST or None, instance=account)
    
    if form.is_valid():
        form.save()
        return redirect("view-account")
        
    return render(request,"ESD_Project/account.html",{"form":form, "account": account})

## club rep functions
def clubrepresentative_view(request):
    club_details = Club.objects.all()
    return render(request, "ESD_Project/clubrepresentative.html",
                  {"club_details": club_details})

def create_member(request):
    form = NewMemberForm(request.POST or None)
    
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("club-representative-view")
    else:
        return render(request, "ESD_Project/create_member.html",{"form": form})

def view_members(request):
    members_list = ClubMember.objects.all()
    return render(request,"ESD_Project/view_members.html",{"members_list": members_list})

def update_member(request,member_id):
    member = ClubMember.objects.get(pk=member_id)
    
    form = NewMemberForm(request.POST or None, instance=member)
    
    if form.is_valid():
        form.save()
        return redirect("view-members")
    
    return render(request,"ESD_Project/member.html",{"member":member,"form": form})

def delete_member(request,member_id):
    member = ClubMember.objects.get(pk=member_id)
    member.delete()
    return redirect("view-members")

## payment details
def view_paymentmethod(request):
    paymentmethod_list = PaymentMethod.objects.all()
    return render(request, "ESD_Project/view_paymentmethods.html",{"paymentmethod_list": paymentmethod_list})

def create_paymentmethod(request):
    form = PaymentMethodForm(request.POST or None)
    
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("view-paymentmethod")
    else:
        return render(request, "ESD_Project/create_paymentmethod.html",{"form":form})

def update_paymentmethod(request,payment_id):
    paymentmethod = PaymentMethod.objects.get(pk=payment_id)
    form = PaymentMethodForm(request.POST or None, instance=paymentmethod)
    
    if form.is_valid():
        form.save()
        return redirect("view-account")
        
    return render(request,"ESD_Project/paymentmethod.html",{"form":form, "paymentmethod": paymentmethod})    


