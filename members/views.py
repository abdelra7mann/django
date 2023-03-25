from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# def members(request):
#     der = loader.get_template('index.html')
#     return HttpResponse(der.render())
# # Create your views here.

# def about(requset):
#     x = {'ahmed':'ahmed aldaa','ahmesd':'ahsvmed alsvaa','ahrrvmed':'ahmsvsded xzalaa', }
#     return render(requset,'about.html',{'name':x})

# def newos(request):
#     return HttpResponse('hello frmo news page ')


# def Services(request):
#     return render(request,'Services.html')



def Contact(request):
    css = '"scss/Csontact.css"'
    return render(request,'Contact.html' ,{'x':css} )

def base(request):
    return render(request,'base.html', {'x':'"css/Contact.css"'})

