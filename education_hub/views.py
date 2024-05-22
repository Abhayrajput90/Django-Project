from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from SingUP.models import SingUPform

# Create your views here.
def index(req):
    return render(req,"index.html")

def courses(req):
    return render(req,"courses.html")

def about(req):
    return render(req,"about.html")

def coursesDtails(req):
    return render(req,"coursesDtails.html")

def contact(req):
    return render(req,"contact.html")

def Spannel(req):
    return redirect("/login/")

def Tpannel(req):
    return redirect("/login/")

# def register(request):
#     # return render(req,"register.html")
#     if request.method == 'POST' :
#         fullName = request.POST['name']
#         email = request.POST['email']
#         Password = request.POST['Password']
#         Cpassword = request.POST['Cpassword']

#     if Password == Cpassword:
#         data = SingUPform.objects.create(name=fullName,email=email,password=Password,cpassword=Cpassword)
#         data.save()
#         return render(request,"index.html")
#     else :
#         print('Password did not match')

        
# def register(request):
#     if request.method == 'POST':
#         fullName = request.POST.get('name')
#         email = request.POST.get('email')
#         password = request.POST.get('Password')
#         cpassword = request.POST.get('Cpassword')
        
#         if not (fullName and email and password and cpassword):
#             messages.error(request, 'Please fill in all fields')
#             return redirect('/register/') 
        
#         if password != cpassword:
#             messages.error(request, 'Passwords do not match')
#             return redirect('/register/') 
        
#         try:
#             data = SingUPform.objects.create(name=fullName, email=email, password=cpassword)
#             data.save()
#             messages.success(request, 'Registration successful')
#             return redirect('/') 
#         except Exception as e:
#             messages.error(request, f'An error occurred: {e}')
#             return redirect('/register/') 
    
#     return render(request, "register.html")

def register(request):
    if request.method == 'POST':
        fullName = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('Password')
        cpassword = request.POST.get('Cpassword')
        option = request.POST.get('option')

        context = {
            'fullName': fullName,
            'email': email,
            'password': password,
            'cpassword': cpassword,
            'option' : option,
        }
        
        if not (fullName and email and password and cpassword and option):
            context['error'] = 'Please fill in all fields'
            return render(request, "register.html", context)
        
        if password != cpassword:
            context['error'] = 'Passwords do not match'
            return render(request, "register.html", context)
        
        try:
            data = SingUPform.objects.create(name=fullName, email=email, password=cpassword, option=option)
            data.save()
            return redirect('/login/') 
        except Exception as e:
            context['error'] = f'An error occurred: {e}'
            return render(request, "register.html", context)
    
    else:
        return render(request, "register.html")


def login(request):
    context ={}
    if request.method == 'POST':
        fullName = request.POST.get('name', '')
        login_email = request.POST.get('email', '')  
        login_password = request.POST.get('password', '') 
        user = SingUPform.objects.filter(email=login_email).first()
        context = {
        'message' : "Login successful!",
        'Name'  : user.name,
        'email'  : user.email,
        'category' : user.option
        }
        if user and user.password == login_password and user and user.option == "Teacher":
            response = render(request,"Tpannel.html", context)
            response.set_cookie("token", login_email, max_age=1728000)
            return response
        
        if user and user.password == login_password and user and user.option == "Student":
            response = render(request,"Spannel.html", context)
            response.set_cookie("token", login_email, max_age=1728000)
            return response
        else:
            context['message'] = 'Invalid login credentials!' if user else 'User does not exist! Please Register Now'

    return render(request, "login.html", context)