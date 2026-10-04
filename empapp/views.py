from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Employee
from django.contrib import messages
from .forms import EmployeeForm
from django.db.models import Max

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        User.objects.create_user(
            username=username,
            password=password
        )

        return redirect('user_login')

    return render(request, 'register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('employee_list')

        return render(request, 'user_login.html', {
            'error': 'Invalid username or password'
        })

    return render(request, 'user_login.html')


def user_logout(request):
    logout(request)
    return redirect('login')
# Create Employees

def employee_create(request):
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form=EmployeeForm()
    return render(request,'employee_form.html',{'form':form})

# READ EMPLOYESS
def employee_list(request):
    employees = Employee.objects.all()
    return render(
        request,
        'employee_list.html',
        {'employees': employees}
    )
def employee_update(request, id):

    employee = get_object_or_404(Employee, id=id)

    if request.method == 'POST':

        form = EmployeeForm(
            request.POST,
            instance=employee
        )

        if form.is_valid():
            form.save()
            return redirect('employee_list')

    else:
        form = EmployeeForm(instance=employee)

    return render(
        request,
        'employee_form.html',
        {'form': form}
    )

# delete emp
def delete_emp(request,id):
    employee = get_object_or_404(Employee, id=id)

    if request.method=='POST':
        employee.delete()
        return redirect('employee_list')
    return render(request,
                   'employee_confirm_delete.html',
                   {'employee':employee})

def about_page(request):
    return render (request,'about_page.html')

def home(request):

    emp_count = Employee.objects.filter(dept='IT').count()

    latest = Employee.objects.latest('id')
    salary = Employee.objects.aggregate(Max('salary'))
    username = request.user.username

    return render(
        request,
        'home.html',
        {
            'username': username,
            'emp_count': emp_count,
            'latest': latest,
            'salary':salary

        }
    )