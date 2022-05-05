"""apna_hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from patient_app import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('search',views.search,name="search"),
    path("about_us/",views.about_us,name="about_us"),
    path("hospital_partners",views.hospital_partners,name="hospital_partners"),
    path("specilist",views.specilist,name="specilist"),
    path("why_ravi",views.why_ravi,name="why_ravi"),
    path("add_patient",views.add_patient,name="add_patient"),
    path("patient_detail/<id>",views.patient_detail,name="patient_detail"),
    path("delete/<id>",views.p_delete,name="p_delete"),
    
]
