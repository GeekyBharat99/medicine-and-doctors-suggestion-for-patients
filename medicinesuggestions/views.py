from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
import urllib
import urllib.request as urllib2
from datetime import date
today = date.today()
authkey = "232419AT2rwRRUo5b77e616"




def Home(request):
    return render(request,'index.html')


def Contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]
        Contactus.objects.create(name=name, email=email, message=message)

    return render(request,'contact.html')

def About(request):
    return render(request,'about.html')


def Services(request):
    return render(request,'services.html')


def Login(request):
    error = False
    if request.method == "POST":
        un = request.POST["un"]
        ps = request.POST["ps"]
        usr = authenticate(username = un, password = ps)
        if usr:
            login(request, usr)
            return redirect("home")
        error = True
    return render(request, "login.html", {"error": error})


def Logout(request):
    logout(request)
    return redirect("login")





def Check(request):
    if request.method == "POST":
        error = False
        d = request.POST
        D = d["disease"]
        Dis = Disease.objects.filter(Name__iexact = D).first()
        if Dis:
            error = False
        else:
            error = True
        data = {
            "Dis":Dis, "error": error
        }
        return render(request, 'check.html', data)

    else:
        return render(request, 'check.html')



def SignUP(request):
    error = False
    if request.method == "POST":
        d = request.POST
        un = d["un"]
        ps = d["ps"]
        email = d["email"]
        number = d["number"]
        usr = User.objects.filter(username = un)

        if not usr:
            user = User.objects.create_user(un, email, ps)
            UserDetails.objects.create(usr=user,
                                       number=number, email=email)
            return redirect("login")
        error = True
    return render(request, "signup.html", {"error":error})


def Response(request):
    respo = Contactus.objects.all()
    d = {
            "data": respo
        }
    return render(request, "Response.html", d)



def Doctor(request):
    error = False
    if request.method == "POST":
        d = request.POST
        name = d["name"]
        email = d["email"]
        disease = d["disease"]
        number = d["number"]
        drs = Doctors.objects.filter(Name = name)

        if not drs:
            Doctors.objects.create(Name = name, specialist = disease, email = email, number = number)
            return redirect("home")
        error = True

    return render(request,"doctor_registration.html", {"error" : error})


def Appointment(request, D_no):
    if request.method == "POST":
        d = request.POST
        name = d["un"]
        time = d["time"]
        D_no = D_no
        mobiles = D_no
        date = today
        user_No = request.user.userdetails_set.first().number
        message = f"You have an appointment with {name} at time {time} on date {date}.if you want to contact Them, {user_No}."
        sender = "TCHSIM"
        route = "4"
        values = {
            'authkey': authkey,
            'mobiles': mobiles,
            'message': message,
            'sender': sender,
            'route': route
        }

        url = "http://api.msg91.com/api/sendhttp.php"
        postdata = urllib.parse.urlencode(values)
        postdata = postdata.encode('ascii')
        req = urllib2.Request(url, postdata)
        response = urllib2.urlopen(req)
        output = response.read()



    return render(request,"appointment.html")


def Appointment_Success(request):
    return render(request,"appointment_sccess.html")