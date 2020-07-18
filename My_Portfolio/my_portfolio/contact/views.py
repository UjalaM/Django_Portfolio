from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.urls import reverse
from contact.models import ContactForm

# Create your views here.
def home(request):
    return render(request,'contact/home.html')

def portfolio(request):
    return render(request,'contact/portfolio.html')

def cont(request):
    return render(request,'contact/cont.html')

def contact_form_submit(request):
    if request.method == "POST":
        name = request.POST['name']
        email_id = request.POST['email_id']
        contact_num = request.POST['contact_num']
        message = request.POST['message']
        ContactForm.objects.create(name=name,
                                   email_id=email_id,
                                   contact_num=contact_num,
                                   message=message,
                                   )
    return HttpResponseRedirect(reverse('contact:cont'))