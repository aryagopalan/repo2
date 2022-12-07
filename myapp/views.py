from django.shortcuts import render

# Create your views here.

def getahome(request):
    return render(request,"home.html")
    
def getaprojects(request):
    return render(request,"projects.html")
def getaprofiles(request):
    return render(request,"profile.html") 
def getaprofiles2(request):
    return render(request,"profile2.html")      
