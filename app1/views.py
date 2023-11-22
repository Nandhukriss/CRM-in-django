from django.shortcuts import render,get_object_or_404,redirect
from .models import Detailsform
# Create your views here.
def index(request):

    
    msg=None
    detail=''
    if request.POST:
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        gender=request.POST.get('gender')
        address=request.POST.get('address')
        pincode=request.POST.get('pincode')
        
        detail=Detailsform(name=name,email=email,phone=phone,gender=gender,address=address,pincode=pincode)
        detail.save()
        msg='User Data Added!'
        detail=Detailsform.objects.all() 
        return render(request,'index.html',{"person":detail,"msg":msg})
    else:
        detail=Detailsform.objects.all() 
    
    return render(request,'index.html',{"person":detail,"msg":msg})
        
def delete(request,id):
    
    obj=get_object_or_404(Detailsform,id=id)
    obj.delete()
        
    return redirect('home')
    
def edit(request,id):
    
    obj=get_object_or_404(Detailsform,id=id)

    if request.POST:
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        gender=request.POST.get('gender')
        address=request.POST.get('address')
        pincode=request.POST.get('pincode')
        
        obj.name=name
        obj.email=email
        obj.phone=phone
        obj.gender=gender
        obj.address=address
        obj.pincode=pincode
        obj.save()
        return redirect('home')

    return render(request,'edit.html',{"obj":obj})
    

    
    

def detail_page(request,id):

    obj=get_object_or_404(Detailsform,id=id)

    return render(request,"details_page.html",{'obj':obj})