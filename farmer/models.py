from django.db import models

# Create your models here.
class market(models.Model):
    market_id=models.AutoField(primary_key=True)
    market_name=models.CharField(max_length=100,default="")
    market_state=models.CharField(max_length=100,default="")
    market_city=models.CharField(max_length=100,default="")
    market_items=models.CharField(max_length=9000,default="")
    pub_date=models.DateField()
    image= models.ImageField(upload_to="farmer/images",default="")

    def __str__(self):
        return self.market_name

class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=70,default="")
    email=models.CharField(max_length=70,default="")
    phone=models.CharField(max_length=20,default="")
    desc=models.CharField(max_length=500,default="")

    def __str__(self):
         return self.name

class farmerupdate(models.Model):
    farmerupdate_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,default="")
    phone=models.CharField(max_length=20,default="")
    email=models.CharField(max_length=100,default="")
    address=models.CharField(max_length=100,default="")
    city=models.CharField(max_length=100,default="")
    state=models.CharField(max_length=100,default="")
    zip_code=models.CharField(max_length=100,default="")
    items=models.CharField(max_length=500,default="")
    weight=models.CharField(max_length=50,default="")
    image= models.ImageField(upload_to="farmer/images",default="")

    def __str__(self):
        return self.name