from django.shortcuts import render,get_object_or_404,redirect
from django.http import JsonResponse
from .models import Detailsform
# Create your views here.
def index(request):

    
    
 
    detail=Detailsform.objects.all() 
    
    return render(request,'index.html',{"person":detail})


def create_data(request):

    if request.POST:
            id = request.POST.get("id")
            print('id',id)
            name=request.POST.get('name')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            gender=request.POST.get('gender')
            address=request.POST.get('address')
            pincode=request.POST.get('pincode')
        
            if id == "":
                detail = Detailsform(name=name,email=email,phone=phone,gender=gender,address=address,pincode=pincode)
            else:
                detail = Detailsform(id=id,name=name,email=email,phone=phone,gender=gender,address=address,pincode=pincode)
            detail.save()

            customer_val = Detailsform.objects.values()
            customer_data = list(customer_val)

            return JsonResponse({"status": "Saved", "customer_data":customer_data})
    else:
        return JsonResponse({"status": "Not Saved"})


    
        
def delete(request):
   
    if request.method == "POST":
        id=request.POST.get('id')
        obj=get_object_or_404(Detailsform,id=id)
        obj.delete()
        return JsonResponse({"status":1})
    else:
        return JsonResponse({"status": 0})
    
def edit(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        print('say',id)
        obj = get_object_or_404(Detailsform, id=id)

        customer_data = {
            "id": obj.id,
            "name": obj.name,
            "email": obj.email,
            "phone": obj.phone,
            "pincode": obj.pincode,
            "gender": obj.gender,
            "address": obj.address
        }

        return JsonResponse(customer_data)
    else:
        # Handle the case when the request method is not POST
        return JsonResponse({"status": "error", "message": "Invalid request method"})

def detail_page(request,id):

    obj=get_object_or_404(Detailsform,id=id)

    return render(request,"details_page.html",{'obj':obj})