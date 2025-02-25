from django.shortcuts import render, redirect



def index(request):
    return render(request, "index.html")

def Apropos(request):
    return render(request, "about.html")

def propriete(request):
    return render(request, "properties.html")

def propert_single(request):
    return render(request, "property-single.html")

def services(request):
    return render(request, "services.html")

def service_detail(request):
    return render(request, "service-details.html")

def contact(request):
    return render(request, "contact.html")




