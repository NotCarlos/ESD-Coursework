from django.db import models

class Club(models.Model):
    clubnumber = models.CharField("Club Number",max_length=10,default=0)
    clubname = models.CharField("Club Name",max_length=120)
    clubrep = models.CharField("Representative", max_length=120)
    password = models.CharField("Password",max_length=120)
    phonenumber = models.CharField("Phone Number",max_length=11,default=0)
    address = models.CharField("Club Address",max_length=200)
    balance = models.CharField("Balance",max_length=100,default=0)
    
    def __str__(self):
        return f"Club: {self.clubname}"
    
class ClubMember(models.Model):
    username = models.CharField("Username",max_length=120)
    fullname = models.CharField("Fullname", max_length=200)
    email = models.EmailField("Email",max_length=200)
    
    def __str__(self):
        return f"Username: {self.username}"
    
class PaymentMethod(models.Model):
    banktype = (("1","..."),("2","Credit"),("3","Debit"))
    
    c_type = models.CharField("Type",max_length=11, choices=banktype, default="1")
    c_name = models.CharField("Holder Name",max_length=120)
    c_number = models.CharField("Card Number",max_length=16)
    c_expireydate = models.CharField("Expire Date",max_length=5)
    
    def __str__(self):
        return f"Holder: {self.c_name}"
    
    