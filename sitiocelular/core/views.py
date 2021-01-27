from core.form import CelularForm,CustomUserForm
from django.shortcuts import render, redirect
from core.models import Celular
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth import login, authenticate

# Create your views here.
def home(request):
    return render(request,'core/home.html')

def galeria(request):
    return render(request,'core/galeria.html')

def listado_celulares(request):
    celulares = Celular.objects.all()
    data = {
        
      'celulares':celulares  
        
        
    }
    return render(request, 'core/listado_celulares.html',data)

#solo los que sean staf o que tengan permiso en especifico del panel del admin de add-celular
@permission_required('core.add_celular') 
def nuevo_celular(request):
    data =  {
        
      'form':CelularForm() 
        
        
    }
    if request.method == 'POST':
        formulario = CelularForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Celular guardado con exito"
    
    
    return render(request,'core/nuevo_celular.html',data)

#@login_required 
@permission_required('core.change_celular')
def modificar_celular(request,id):
    celular = Celular.objects.get(id = id)
    data = {
        
      'form':CelularForm(instance = celular)
        
    }
    if request.method == 'POST':
        formulario = CelularForm(data = request.POST, instance=celular)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'celular modificada correctamente'
            data['form'] = formulario

    return render(request, 'core/modificar_celular.html', data)

@login_required
def eliminar_celular(request,id):
    celular = Celular.objects.get(id = id)
    celular.delete()
    return redirect(to="listado_celulares")


def registro_usuario(request):
    
    data = {

        'form':CustomUserForm()

    }

    if request.method == 'POST':

        formulario = CustomUserForm(request.POST)

        if formulario.is_valid():

            formulario.save()

            # recordar from django.contrib.auth import login, authenticate

            username = formulario.cleaned_data['username']

            password = formulario.cleaned_data['password1']

            user = authenticate(username= username, password=password)

            login(request, user)

            return redirect(to='home')



    return render(request, "registration/registrar.html", data)