from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
from app1.models import Usuarios
from app1.forms import UsuariosForm
from django.shortcuts import render, redirect, get_object_or_404


# registro de usuarios



# index


def inicio(request):
    # Otras operaciones si es necesario
    return render(request, 'index.html')



# registro

def registro(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellidos = request.POST.get('apellidos')
        celular = request.POST.get('celular')
        email = request.POST.get('email')
        direccion = request.POST.get('direccion')
        contrasena = request.POST.get('contrasena')


        # Hash the password before saving it to the database
        contrasena_hasheada = make_password(contrasena)

        # Create a new user with the data provided

        # Hashear la contraseña antes de guardarla en la base de datos
        contrasena_hasheada = make_password(contrasena)

        # Crear un nuevo usuario con los datos proporcionados

        nuevo_usuario = Usuarios(nombre=nombre, apellidos=apellidos, celular=celular, email=email, direccion=direccion, contrasena=contrasena_hasheada)
        nuevo_usuario.save()

        messages.success(request, '¡Usuario registrado exitosamente!')
        return render(request, 'registro.html')
    else:

        messages.success(request, '¡Ya estás registrado!')
        
        messages.success(request, '¡ya estas registrado!')
        return render(request, 'registro.html')
    

    
#  crud completo 



def lista_usuarios(request):
    usuarios = Usuarios.objects.all()
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios})

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuariosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuariosForm()
    return render(request, 'crear_usuario.html', {'form': form})

def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuarios, pk=pk)
    if request.method == 'POST':
        form = UsuariosForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuariosForm(instance=usuario)
    return render(request, 'editar_usuario.html', {'form': form, 'usuario': usuario})

def eliminar_usuario(request, pk):
    usuario = get_object_or_404(Usuarios, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_usuarios')
    return render(request, 'confirmar_eliminar.html', {'usuario': usuario})



# login


from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.shortcuts import render


def valida_login(request):
    if request.method == 'POST':
        usu = request.POST.get('email')
        contra = request.POST.get('contrasena')
     
        if Usuarios.objects.filter(email=usu).exists():
            logueo = Usuarios.objects.get(email=usu)
            passw = check_password(contra, logueo.contrasena)
            
            if passw:
                request.session['seguridad'] = True
                return render(request, 'index.html')
            else:
                messages.error(request, 'Usuario o contraseña incorrecta')
                return render(request, 'login.html')
        else:
            messages.error(request, 'Usuario no encontrado')
            return render(request, 'login.html')
    
    return render(request, 'login.html')

# Vista para listar todos los usuarios

def listar_usuarios(request):
    usuarios = Usuarios.objects.all()
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})

# Vista para crear un nuevo usuario

def agregar_usuario(request):
    if request.method == 'POST':
        formulario = AddUsuariosForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Usuario creado exitosamente')
            return redirect("listar_usuarios")  # Reemplaza "listar_usuarios" con la URL adecuada
    else:
        formulario = AddUsuariosForm()
    
    return render(request, 'agregar_usuario.html', {'formulario': formulario})

# Vista para editar un usuario

def form_editar_usuario(request, id):
    usuario = get_object_or_404(Usuarios, idestudios=id)
    if request.method == 'POST':
        formulario = AddUsuariosForm(request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Usuario editado exitosamente')
            return redirect("listar_usuarios")  # Reemplaza "listar_usuarios" con la URL adecuada
    else:
        formulario = AddUsuariosForm(instance=usuario)
    
    return render(request, 'editar_usuario.html', {'formulario': formulario, 'usuario': usuario})

# Vista para eliminar un usuario

def eliminar_usuario(request, id):
    usuario = get_object_or_404(Usuarios, idestudios=id)
    if request.method == 'POST':
        usuario.delete()
        messages.success(request, 'Usuario eliminado exitosamente')
        return redirect("listar_usuarios")  # Reemplaza "listar_usuarios" con la URL adecuada
    
    return render(request, 'eliminar_usuario.html', {'usuario': usuario})
