from django.shortcuts import render

from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from website.forms import ContactForm,NewsletterForm
from django.contrib import messages
from blog.models import Post


def home(request):
    posts = Post.objects.filter(status=1)
    context={'posts':posts}
    return render(request,'website/index.html',context)

def about(request):
    return render(request,'website/about.html')

def contact(request):
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Your Message has been sent Successfully")
        else:
            messages.add_message(request, messages.ERROR, "Your message was not sent successfully")
    form=ContactForm()
    return render(request,'website/contact.html')

def newsletter(request):
    if request.method == 'POST':
        form=NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
    
def elements(request):
    return render(request,'website/elements.html')
