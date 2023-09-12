from django.shortcuts import redirect, render
from . forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm


from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from .models import Record
from django.contrib import messages

# главная страница
def frontpage(request):
    return render(request, 'core/frontpage.html')

# регистраця пользователя
def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()
            
            messages.success(request, 'Вы успешно зарегистрировались!')

            return redirect('login')
    else:
        form=CreateUserForm()
    
    context= {
        "form": form
    }

    return render(request, 'core/signup.html', context)


# вход пользователя
def login(request):
    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("dashboard")

    context = {'form':form}

    return render(request, 'core/login.html', context=context)


# страница пользователя
@login_required(login_url='login')
def dashboard(request):
    records=Record.objects.all()

    context={
        "records": records
    }
    return render(request, 'core/dashboard.html', context)


@login_required(login_url='login')
def create_record(request):

    form=CreateRecordForm()
    
    if request.method == 'POST':

        form = CreateRecordForm(request.POST)
        
        if form.is_valid():
            form.save()

            messages.success(request, 'Запись успешно создана')
        
            return redirect('dashboard')

    context= {
        "form": form
    }

    return render(request, 'core/create-record.html', context)

@login_required(login_url='login')
def update_record(request, pk):
    record=Record.objects.get(id=pk)
    
    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():
            form.save()
            messages.success(request, 'Запись успешно обнавлена')
            return redirect('dashboard')
    else:
        form=UpdateRecordForm(instance=record)

    context= {
        "form": form
    }

    return render(request, 'core/update-record.html', context)

@login_required(login_url='login')
def singular_record(request, pk):
    all_records=Record.objects.get(id=pk)

    context= {
        "record": all_records
    }

    return render(request, 'core/view-record.html', context)
    
# удалить запись
@login_required(login_url='login')
def delete_record(request, pk):
    record=Record.objects.get(id=pk)
    record.delete()
    
    messages.success(request, 'Вы удалили запись')
    return redirect('dashboard')
    


# выход пользователя
def logout(request):
    auth.logout(request)
    
    messages.success(request, 'Вы успешно вышли из системы')
    
    return redirect('login')
