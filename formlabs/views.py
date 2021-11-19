from django.shortcuts import render, redirect

from formlabs.models import Cliente

def list(request):
    list_=Cliente.objects.all()
    return  render(request, 'impresoras/index.html', {'list':list_})

def save(request):

    if "GET" == request.method:
        return render(request,  'impresoras/index.html')

    nombre_=request.POST["nombre"]
    apellido_=request.POST["apellido"]
    correo_=request.POST["correo"]
    telefono_=request.POST["telefono"]
    industria_=request.POST["industria"]
    empresa_= request.POST["empresa"]
    trabajo_= request.POST["trabajo"]

    cliente =Cliente(nombre=nombre_, apellido=apellido_, correo=correo_, telefono=telefono_, industria=industria_, empresa=empresa_, trabajo=trabajo_)
    cliente.save()


    return render(request,  'impresoras/index.html')