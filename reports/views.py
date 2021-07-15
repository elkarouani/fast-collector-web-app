from django.http import HttpResponse

def FormView(request): return HttpResponse("Form Page")

def ExportView(request): return HttpResponse("Export Page")
