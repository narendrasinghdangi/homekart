from django.db import models

# Create your models here.
class Productl(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category= models.CharField(max_length=50, default="")
    sub_category= models.CharField(max_length=50, default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=700)
    pub_date=models.DateField()
    image= models.ImageField(upload_to="homekart/images",default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=70,default="")
    email=models.CharField(max_length=70,default="")
    phone=models.CharField(max_length=20,default="")
    desc=models.CharField(max_length=500,default="")

    def __str__(self):
         return self.name

class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=5000,default="")
    name=models.CharField(max_length=100,default="")
    email=models.CharField(max_length=100,default="")
    address=models.CharField(max_length=100,default="")
    city=models.CharField(max_length=100,default="")
    state=models.CharField(max_length=100,default="")
    zip_code=models.CharField(max_length=100,default="")
    phone=models.CharField(max_length=100,default="")

    def __str__(self):
        return self.name

class orderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default="")
    update_desc=models.CharField(max_length=5000)
    timestamp=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:12]+"..."