from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.
def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('members.html')
    
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))
    
# 
# display members details
def memberdetails(request, id):
    mymember = Member.objects.get(id=id)
    # template = loader.get_template('details.html')
    
    context = {
        'mymember': mymember,
    }
    return render(request, 'details.html', context)
    # return HttpResponseRedirect(template.render(context, request))

# index page
def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
    
# testing view
def testing(request):
    template = loader.get_template('testing.html')
    
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry'],
        'count': len(['Apple', 'Banana']),
    }
    return HttpResponse(template.render(context, request))










# template = loader.get_template('hello.html')
# return HttpResponse(template.render())
# return HttpResponse("Hello world")

