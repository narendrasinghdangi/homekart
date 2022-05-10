from math import ceil
from django.http import HttpResponse
from django.shortcuts import render
from .models import Productl,Contact,Orders,orderUpdate
import json

# Create your views here.
def index(request):
    #pro = Productl.objects.all()
    #n = len(pro)
    #nslide = n//4+ceil((n/4)-(n//4))
    #params={'no_of_slide':nslide,'range':range(1,nslide), 'product':pro}
    #allprods =[[pro,range(1,nslide),nslide],
    #           [pro,range(1,nslide),nslide]]
    allprods = []
    catprods = Productl.objects.values('category')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod=Productl.objects.filter(category=cat)
        n = len(prod)
        nslide = n//4+ceil((n/4)-(n//4))
        allprods.append([prod,range(1,nslide),nslide])
    params={'allprods':allprods}
    return render(request,'homekart/index.html',params)

def about(request):
    return render(request,'homekart/about.html')

def contact(request):
    if request.method=="POST":
        namet=request.POST.get('name','')
        emailt=request.POST.get('email','')
        phonet=request.POST.get('phone','')
        desct=request.POST.get('desc','')
        contact=Contact(name=namet,email=emailt,phone=phonet,desc=desct)
        contact.save()
    return render(request,'homekart/contact.html')

def tracker(request):
    if request.method=="POST":
        orderId=request.POST.get('orderId','')
        email=request.POST.get('email','')
        try:
            order=Orders.objects.filter(order_id=orderId,email=email)
            if len(order)>0:
                update=orderUpdate.objects.filter(order_id=orderId)
                updates=[]
                for item in update:
                    updates.append({'text':item.update_desc,'time':item.timestamp})
                    response=json.dumps([updates,order[0].items_json],default=str)
                return HttpResponse(response)
            else:
                return HttpResponse("{}")
        except Exception as e:
            return HttpResponse("{}")
    return render(request,'homekart/tracker.html')
    
def search(request):
    return render(request,'homekart/search.html')

def productView(request,myid):
    product=Productl.objects.filter(id=myid)
    return render(request,'homekart/prodView.html',{'product':product[0]})

def checkout(request):
    if request.method=="POST":
        items_json=request.POST.get('itemsJson','')
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        address=request.POST.get('address1','')+" "+request.POST.get('address2','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zip_code=request.POST.get('zip_code','')
        phone=request.POST.get('phone','')
        order=Orders(items_json=items_json,name=name,email=email,address=address,city=city,state=state,zip_code=zip_code,phone=phone)
        order.save()
        update=orderUpdate(order_id=order.order_id,update_desc="your order is successfully placed")
        update.save()
        thank=True
        id=order.order_id
        return render(request,'homekart/checkOut.html',{'thank':thank,'id':id})
    return render(request,'homekart/checkOut.html')