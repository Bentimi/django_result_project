from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm, LoginFormuser, CreateuserForm, UpdateuserForm, import_data
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import user
from tablib import Dataset
from .resources import UserResource
from django.contrib import messages

# from import_export.formats import base_formats
# from import_export.admin import ImportMixin, ExportMixin

# Create your views here.

def home(request):
    return render(request, 'index.html')

def form(request):
    return render(request, 'form.html')


# register view
def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('my_login')
    context = {'form':form}   
    return render(request, 'register.html', context=context)

# # Login a User
def my_login(request):
    form = LoginFormuser()

    if request.method == 'POST':
        form = LoginFormuser(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            log = authenticate(request, username=username, password=password)

            if log is not None:
                auth.login(request, log)
                if log.is_authenticated and log.is_superuser:
                    return redirect('dashboard')
                elif log.is_authenticated:
                    return redirect('portal')

    context = {'form2':form}

    return render(request, 'login.html', context=context)

# User Logout
@login_required(login_url="my_login")
def user_logout(request):
    auth.logout(request)

    return redirect("my_login")

# Dashboard
@login_required(login_url='my_login')
def Dashboard(request):
    if 'filter' in request.GET:
        q = request.GET['filter'] 
        id = user.objects.filter(id__icontains=q)
        first_name = user.objects.filter(first_name__icontains=q)
        last_name = user.objects.filter(last_name__icontains=q)
        matric_number = user.objects.filter(matric_number__icontains=q)
        course = user.objects.filter(course__icontains=q)
        course = user.objects.filter(course__icontains=q)
        context={
                'records' :  id or first_name or last_name or matric_number or course

                }
    
    elif 'all' in request.GET:
        fetch_data = user.objects.all()
        context={'records' : fetch_data}

    else:
        my_records = user.objects.all()
        context={'records': my_records}

    return render(request, 'dashboard.html', context=context)
    
# CREATE RRECORD
@login_required(login_url='my_login')
def create_record(request):
    
    form = CreateuserForm
    ()

    if request.method == 'POST':
        form = CreateuserForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect("dashboard")
    
    context = {'form' : form}
    return render(request, 'create-record.html', context=context)
    

# UPDATE RRECORD
@login_required(login_url='my_login')
def update_record(request, pk):
    
    record = user.objects.get(id=pk) 

    form = UpdateuserForm(instance=record)

    if request.method == 'POST':
        form = UpdateuserForm(request.POST, instance=record)

        if form.is_valid():
            form.save()

            return redirect('dashboard')
    context = {'form' : form}
    return render(request, 'update-record.html', context=context)

# Read or View Singular Record
@login_required(login_url='my_login')
def Singular_record(request, pk):

    all_records = user.objects.get(id=pk)

    context = {'record' : all_records}

    return render(request, 'view-record.html', context=context)

# Delete Record
@login_required(login_url='my_login')
def delete_record(request, pk):

    record = user.objects.get(id=pk)

    record.delete()

    return redirect('dashboard')

@login_required(login_url='my_login')
def portal(request):
    if request.method == 'POST':
        matric_number = request.POST['matric_number']
        course = request.POST['course']
        try:
            my_records = user.objects.get(matric_number=matric_number, course=course)
            percent = int(my_records.score)
            percentage = (percent/30)*100
            if int(my_records.score) >=21:
                color = 'success'
                status = 'Strong'
            elif int(my_records.score) >= 15:
                color = 'primary'
                status = 'Fair'
            elif int(my_records.score) >= 10:
                color = 'warning'
                status = 'Weak'
            elif int(my_records.score) >= 0:
                color = 'danger'
                status = 'poor'
            context={'records': my_records,
                     'percentage': percentage,
                     'color': color,
                     'status' : status
                     } 
            return render(request, 'result.html', 
            context=context)
       
        except user.MultipleObjectsReturned:
            msg = 'Internal Error Occured!'
            context = {'error_message': msg}
            return render(request, 'portal.html', context=context)
        except :
            msg = 'Try again, invalid Input!'
            context = {'error_message': msg}
            return render(request, 'portal.html', context=context)


    return render(request, 'portal.html')

@login_required(login_url='my_login')
def file(request):
    if request.method == 'POST':
        try:
            import_resource = UserResource()
            dataset = Dataset()
            data_input = request.FILES['upload']
            imported_data = dataset.load(data_input.read(), format='xlsx')
            for data in imported_data:
                value = user(
                    data[0], # ID
                    data[1], # FIRST_NAME
                    data[2], # LAST_NAME
                    data[3], #MATRIC_NUMBER
                    data[4], # COURSE
                    data[5], # SCORE
                    data[6] # STATUS
                )
                value.save()
                message = "File Successfully Uploaded!"
                bg = 'success'
                context = {
                    'message': message,
                    'bg': bg
                }
            return render(request, 'file.html', context=context)
        except:
            message = "File Must Be in xlsx or xls Format Only!"
            bg = 'danger'
            context = {
                    'message': message,
                        'bg': bg
                    }
            return render(request, 'file.html',     context=context)

    else:            

        message = "NOTE: File Must Be in xlsx or xls Format!"
        bg = 'warning'
        context = {
                    'message': message,
                    'bg': bg
                }

    return render(request, 'file.html', context=context)


def nav(request):
    return render(request, 'nav.html')