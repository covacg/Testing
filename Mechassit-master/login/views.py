from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User


from .forms import createUserForm, UserProfileForm, VehiculoForm, UserEditForm
from .models import ExtendedData,Vehiculos

# Create your views here.

####################CLIENTES####################
# VISTA PARA EL LOGIN
def home_login(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        contrasena = request.POST.get('contrasena')

        # Autenticar al usuario con las credenciales proporcionadas
        user = authenticate(request, username=correo, password=contrasena)

        if user is not None:
            # Verificar si el usuario es cliente o taller basado en la existencia de cp en ExtendedData
            try:
                usuario_extendido = user.extendeddata
                if usuario_extendido.cp:
                    # Es taller, redirige a cliente_calendario.html
                    login(request, user)  
                    return render(request,'taller_edit.html')  
                else:
                   
                    login(request, user)  
                    return render(request,'clientes_edit.html')  
            except ExtendedData.DoesNotExist:
                pass

    return render(request, 'login.html')


#VISTA PARA REGISTRAR TALLER
def taller(request):
    user_form = createUserForm()
    user_profile_form = UserProfileForm()
    data_context = {'user_form': user_form, 'user_profile_form': user_profile_form}
    if request.method == 'POST':
        user_form = createUserForm(request.POST)
        user_profile_form = UserProfileForm(request.POST)
        print(user_form.errors)
        print(user_profile_form.errors)
        if user_form.is_valid() and user_profile_form.is_valid():
            user = user_form.save() 
            profile = user_profile_form.save(commit=False)  
            profile.user = user
            profile.save()
            return render(request, 'login.html')
    return render(request, 'taller.html', data_context)


#VISTA PARA REGISTRAR CLIENTE
def cliente(request):
    user_form = createUserForm()
    user_profile_form = UserProfileForm()
    data_context = {'user_form': user_form, 'user_profile_form': user_profile_form}
    if request.method == 'POST':
        user_form = createUserForm(request.POST)
        user_profile_form = UserProfileForm(request.POST)
        print(user_form.errors)
        print(user_profile_form.errors)
        if user_form.is_valid() and user_profile_form.is_valid():
            user = user_form.save() 
            profile = ExtendedData()
            profile.telefono = request.POST['telefono']
            profile.direccion = request.POST['direccion']
            profile.cp = request.POST['cp']
            profile.user = user
            profile.save()
            return render(request, 'login.html')
    return render(request, 'cliente.html', data_context)
####################LOGIN####################



####################CLIENTES####################
@login_required
def clientes_calendario(request):
    return render(request, 'clientes_calendario.html') 

@login_required
def clientes_talleres(request):
    return render(request, 'clientes_talleres.html') 

#EDITAR PERFIL
@login_required
def clientes_edit(request):
    user = request.user
    try:
        extended_data = ExtendedData.objects.get(user=user)
    except ExtendedData.DoesNotExist:
        extended_data = None

    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()

            telefono = form.cleaned_data['telefono']
            if extended_data:
                extended_data.telefono = telefono
                extended_data.save()
            else:
                ExtendedData.objects.create(user=user, telefono=telefono)

            return redirect('cperfil')

    else:
        form = UserEditForm(instance=user, initial={'telefono': extended_data.telefono if extended_data else None})

    return render(request, 'clientes_edit.html', {'form': form, 'extended_data': extended_data})

#VEHÍCULOS
@login_required
def clientes_vehiculos(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            vehiculo = form.save(commit=False)
            vehiculo.usuario = request.user
            vehiculo.save()
            return redirect('cvehiculos')

    else:
        form = VehiculoForm()

    vehiculos = Vehiculos.objects.filter(usuario=request.user)
    return render(request, 'clientes_vehiculos.html', {'form': form, 'vehiculos': vehiculos})

#PENDIENTE PARA EL PRÓXIMO SPRINTT
@login_required
def clientes_notificacion(request):
    return render(request, 'clientes_notificacion.html') 
####################CLIENTES####################


#PINTAR PÁGINA DE SI ERES TALLER O CLIENTE
def register_option(request):
    return render(request,'registeroption.html')



####################TALLERES####################
@login_required
def talleres_edit(request):
    return render(request,'taller_edit.html')

@login_required
def talleres_notificacion(request):
    return render(request,'taller_notificacion.html')


@login_required
def talleres_servicios(request):
    return render(request,'taller_servicios.html')

@login_required
def talleres_citas(request):
    return render(request,'taller_citas.html')

@login_required
def talleres_analitica(request):
    return render(request,'taller_analitica.html')


