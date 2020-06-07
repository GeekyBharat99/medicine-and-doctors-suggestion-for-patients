from medicinesuggestions.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", Home, name="home"),
    path("contact/", Contact, name="contact"),
    path("services/", Services, name="services"),
    path("about/", About, name="about"),
    path("check/", Check, name="check"),
    path("login/", Login, name="login"),
    path("logout/", Logout, name="logout"),
    path("signup/", SignUP, name="signup"),
    path("response/", Response, name="response"),
    path("appointment_success/", Appointment_Success, name="appointment_success"),
    path("appointment/<int:D_no>/", Appointment, name="appointment"),
    path("Doctors_registration/", Doctor, name="Doctors_registration"),

]
