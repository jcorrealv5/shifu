from django.shortcuts import render

def Paint(request):    
    return render(request, "wsDemo03/Paint.html")