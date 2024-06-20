from django.shortcuts import render
from cargarcontenido.models import *

def contenido_videos(request):
    videos= Video.objects.all()
    return render(request,'contenidoalumno/videos.html',{'videos':videos})

def contenido_documentos(request):
    documentos= Documento.objects.all()
    return render(request,'contenidoalumno/documentos.html',{'documentos':documentos})

def contenido_textos(request):
    textos= Resumen.objects.all()
    return render(request,'contenidoalumno/textos.html',{'textos':textos})