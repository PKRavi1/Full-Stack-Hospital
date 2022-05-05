from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Patient
# Create your views here.
def home(request):
    return render(request,"home.html")

def search(request):
    all_user=Patient.objects.all()
    query=request.GET.get('q')          #searching patient information
    if query:                   #searching information
        all_user=Patient.objects.filter(name__icontains=query)      #searching patient information
    return render(request,"search.html",{"ul":all_user})  #here ul is keyword and all_user is variable
  
def patient_detail(request,id):                   #this is use for getting patient id
    user_detail=Patient.objects.get(id=id)
    return render(request,"patient_detail.html",{"ud":user_detail})

def about_us(request):
    return render(request,"about_us.html")

def hospital_partners(request):
    return render(request,"hospital_partners.html")

def specilist(request):
    return render(request,"specilist.html")

def why_ravi(request):
    return render(request,"why_ravi.html")

def delete(request):
    return render(request,"delete.html")

def p_delete(request,id):
    p=get_object_or_404(Patient,id=id)            #this is use for delete patient id
    if request.method=="POST":
        p.delete()
        return search(request)
    else:
        return render(request,"delete.html")

def add_patient(request):                  #this is use for getting input from user side
    if request.method=="POST":
        Patient_name=request.POST['name']
        P_mobile=request.POST['mobile']
        P_aadhar=request.POST['aadhar']
        P_date_of_birth=request.POST['date_of_birth']
        P_address=request.POST['address']
        P_email=request.POST['email']

        patient, created =Patient.objects.get_or_create(         #create for Retriving

         name= Patient_name,
         mobile=P_mobile,
         aadhar=P_aadhar,
         date_of_birth=P_date_of_birth,
         address=P_address,
         email=P_email,
        )
        return search(request)
    else:
        return render(request,"add_patient.html")

