from django import forms
from django.forms import ModelForm
from ESD_Project.models import ClubMember, Club, PaymentMethod

class ClubForm(ModelForm):
    class Meta:
        model = Club
        fields = ("clubname","clubrep","password","phonenumber","address")

class NewMemberForm(ModelForm):
    class Meta:
        model = ClubMember
        fields = "__all__"
        
class PaymentMethodForm(ModelForm):
    class Meta:
        model = PaymentMethod
        fields = "__all__"