from django.shortcuts import render,redirect
from cargarcontenido.models import *
from django.conf import settings
import os
from django.core.files.storage import FileSystemStorage
from .forms import VideoForm
from datetime import datetime


def index(request):
    resumenes= Resumen.objects.all()
    documentos=Documento.objects.all()
    videos=Video.objects.all()
    return render(request, 'cargarcontenido/index.html',context={
        'documentos':documentos,'resumenes':resumenes,'videos':videos
    })

def documento_create(request):
    return render(request, 'cargarcontenido/documento_create.html')

def resumen_create(request):
    return render(request, 'cargarcontenido/resumen_create.html')

def video_create(request):
    return render(request,'cargarcontenido/video_create.html')

def video_store(request):
    nombre=request.POST.get('nombre')
    video=request.FILES.get('video')
    
    if request.method=='POST' and request.FILES['video']:
        myfile=request.FILES['video']

        now = datetime.now()
        datetime_str = now.strftime("%Y%m%d%H%M%S")
        original_filename = myfile.name
        filename_pre=original_filename.split('.')[0]
        extension = original_filename.split('.')[-1]
        unique_filename = filename_pre+"_"+datetime_str+"."+extension

        fs=FileSystemStorage()
        filename=fs.save(unique_filename,myfile)
        uploaded_file_url=fs.url(filename)#la url del archivo cargado
        
        obj=Video()
        obj.nombre=nombre
        obj.video=unique_filename
        obj.save()
        return redirect('cargarcontenido.index')

def resumen_store(request):
    nombre=request.POST.get('nombre')
    resumen=request.POST.get('resumen')
    obj=Resumen()
    obj.nombre=nombre
    obj.resumen=resumen
    obj.save()

    return redirect('cargarcontenido.index')

def resumen_update(request):
    id_resumen=request.POST.get('id_resumen')
    nombre=request.POST.get('nombre')
    resumen=request.POST.get('resumen')
    resumen_ai=request.POST.get('resumen_ai')
    obj=Resumen.objects.get(id=id_resumen)
    obj.nombre=nombre
    obj.resumen=resumen
    obj.resumen_ai=resumen_ai
    obj.save()
    return redirect('cargarcontenido.index')

def resumen_edit(request,id):
    resumen=Resumen.objects.get(id=id)
    return render(request,'cargarcontenido/resumen_edit.html',{'resumen':resumen})


def documento_store(request):
    nombre=request.POST.get('nombre')
    archivo=request.FILES.get('archivo')
    now = datetime.now()

    if request.method=='POST' and request.FILES['archivo']:
        myfile=request.FILES['archivo']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        uploaded_file_url=fs.url(filename)
        
        obj=Documento()
        obj.nombre=nombre
        obj.archivo=archivo
        obj.save()

    return redirect('cargarcontenido.index')
    
def documento_edit(request,id):
    documento=Documento.objects.get(id=id)
    return render(request,'cargarcontenido/documento_edit.html',{'documento':documento})

def documento_update(request):
    id_documento=request.POST.get('id_documento')
    nombre=request.POST.get('nombre')
    archivo=request.FILES.get('archivo')
    now = datetime.now()

    if request.method=='POST':
        obj=Documento.objects.get(id=id_documento)
        
        myfile=request.FILES['archivo']
        fs=FileSystemStorage()
        
        if request.FILES['archivo']:
            documento_borrar=os.path.join(settings.MEDIA_ROOT, obj.archivo)
            if os.path.exists(documento_borrar):
                os.remove(documento_borrar)
                print("borrado....")
    
        filename=fs.save(myfile.name,myfile)
        uploaded_file_url=fs.url(filename)
        
        obj.nombre=nombre
        obj.archivo=archivo
        obj.resumen_ai='-'
        obj.contenido_texto='-'
        obj.save()

    return redirect('cargarcontenido.index')
    