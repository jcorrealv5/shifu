from django.shortcuts import render

def Chat(request):    
    return render(request, "wsDemo02/Chat.html")