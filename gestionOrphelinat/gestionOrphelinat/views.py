from django.shortcuts import render

# from django.contrib import messages
# # Create your views here.
def PageAccueil(request):
    return render(request, 'index.html')
#===================================================
#===================================================
def About(request):
    return render(request, 'about.html')
#===================================================
def Contact(request):
    return render(request, 'contact.html')
#===================================================
def Gallery(request):
    return render(request, 'gallery.html')
#===================================================
def Services(request):
    return render(request, 'services.html')
#=================================================

