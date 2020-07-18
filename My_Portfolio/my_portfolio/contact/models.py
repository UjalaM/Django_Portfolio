# Create your models here.
from django.db import models
from django.utils import timezone

class ContactForm(models.Model):

    #This field store Full Name 
    name = models.CharField(max_length=300,blank=True)
    #This field store Email ID
    email_id = models.CharField(max_length=300,blank=True)
    #This field store Contact Number 
    contact_num = models.CharField(max_length=300,blank=True)
    #This field store Message 
    message = models.TextField(max_length=3000,blank=True)
    #This field store Date & Time at which form is submitted
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.pk) #Return Primary Key

    class Meta:
        verbose_name_plural = "Contact Form Data"
        verbose_name = "Contact Form"

