from django.http import HttpResponse
from django.shortcuts import render
from .models import farmerupdate, market,Contact
from math import ceil

def index(request):
    allprods = []
    catprods = market.objects.values('market_state')
    cats = {item['market_state'] for item in catprods}
    cats=sorted(cats)
    for cat in cats:
        prod=market.objects.filter(market_state=cat)
        n = len(prod)
        nslide = n//4+ceil((n/4)-(n//4))
        allprods.append([prod,range(1,nslide),nslide])
    params={'allprods':allprods}
    return render(request,'farmer/index.html',params)


def about(request):
    return render(request,'farmer/about.html')

def search(request):
    return render(request,'farmer/search.html')

def productView(request,id):
    product=market.objects.filter(market_id=id)
    return render(request,'farmer/prodView.html',{'product':product[0], 'products': product[0].market_items.split(" ")})

def contact(request):
    if request.method=="POST":
        namet=request.POST.get('name','')
        emailt=request.POST.get('email','')
        phonet=request.POST.get('phone','')
        desct=request.POST.get('desc','')
        contact=Contact(name=namet,email=emailt,phone=phonet,desc=desct)
        contact.save()
    return render(request,'farmer/contact.html')

def success(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        phone=request.POST.get('phone','')
        email=request.POST.get('email','')
        address=request.POST.get('address1','')+" "+request.POST.get('address2','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zip_code=request.POST.get('zip_code','')
        items=request.POST.get('items','')
        weight=request.POST.get('qty','')
        farmerup=farmerupdate(name=name,phone=phone,email=email,address=address,city=city,state=state,zip_code=zip_code,items=items,weight=weight)
        farmerup.save()
        return render(request,'farmer/success.html')
    else:
        return HttpResponse("Error occurred. please Try again")