#------Django Internal Packages-----
from django.contrib import admin
from django.urls import path
#/------Django Internal Packages-----


#<-------- importing view from my_portfolio_website_app -------------
from contact import views
#</-------- importing view from my_portfolio_website_app -------------

#App Name in the project
app_name='contact'



urlpatterns = [
    
    #Url for about view 
    path('',views.home,name='home'),

    #Url for portflio view
    path('portfolio',views.portfolio,name='portfolio'),

    #Url for contact view
    path('contact',views.cont,name='cont'),

    #Url for Contcat form submit view
    path('contact_form_submit',views.contact_form_submit,name='contact_form_submit'),

]