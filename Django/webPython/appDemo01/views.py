from django.http import HttpResponse

def Inicio(request):    
    html = "<body bgColor='aqua'>"
    html += "<h1>Demo 01: Mi Primera Pagina</h1>"
    html += "<h2>Copiado: Jhon Correal</h2>"
    html += "<img src='https://media.istockphoto.com/id/950841682/es/foto/imagen-de-concepto-de-cables-y-conexiones-para-la-transferencia-de-datos-en-la-prestaci%C3%B3n-de.jpg?s=612x612&w=0&k=20&c=w6jv2cH4DoDRpOuEhlslKR7aAkl1l5bNeLxDQl4arRg=' />"
    html += "</body>"
    return HttpResponse(html)