from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def configuration(request):
    return HttpResponse("Configuración")

def human_resources(request):
    return HttpResponse("Recursos humanos")

def company(request):
    return HttpResponse("Compañia")

def production(request):
    return HttpResponse("Producción")

def finance(request):
    return HttpResponse("Finanzas")

def crm(request):
    return HttpResponse("CRM")

def websites(request):
    return HttpResponse("Sitios Web")

def proyects(request):
    return HttpResponse("Proyectos")

def sales(request):
    return HttpResponse("Ventas")