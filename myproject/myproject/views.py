from django.shortcuts import render ,redirect
from myproject.models import *
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from .froms import RegisterFrom

def index(request):
    produc = Producto.objects.all()    
    return render(request,'index.html',{'productos':produc })


def login_view(request): 
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        passw = request.POST.get('passw')

        user = authenticate(usuario=usuario, passw=passw)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.usuario))
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña no validos')
                                
    return render(request,'login.html',{    
     })


def logout_view(request):
    logout(request)
    messages.success(request, 'Sesion cerrada exitosamente')
    return redirect('login')
    

def registro(request):
        form = RegisterFrom(

                   
        )
        
        if request.method == 'POST':
            pass
            
        return render(request,'registro.html',{
            'form': form
    })

def resgistro1(requet):
    return render(requet, 'registro1.html',{
    })


