from django.urls import path
from ESD_Project import views

# add links to web pages in urlpatterns

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    
    path("club-representative/", views.clubrepresentative_view, name="club-representative-view"),
    path("club-representative/create-member", views.create_member, name="create-member"),
    path("club-representative/view-members", views.view_members, name="view-members"),
    path("club-representative/update-member/<member_id>", views.update_member, name="update-member"),
    path("club-representative/delete-member/<member_id>",views.delete_member, name="delete-member"),
    
    path("club-representative/view-account", views.view_account, name="view-account"),
    path("club-representative/update-account/<account_id>", views.update_account, name="update-account"),
    
    path("club-representative/view-paymentmethod", views.view_paymentmethod, name="view-paymentmethod"),
    path("club-representative/create-paymentmethod", views.create_paymentmethod, name="create-paymentmethod"),
    path("club-representative/update-paymentmethod/<payment_id>", views.update_paymentmethod, name="update-paymentmethod"),

]