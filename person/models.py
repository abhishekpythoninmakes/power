from django.db import models


class District(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class City(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=124)
    dob = models.DateField(default=None)
    age = models.IntegerField()
    roles = (('male',"Male"),('female',"Female"),('trans',"Trans"))
    gender = models.CharField(max_length=10,choices=roles,default="male")
    number = models.CharField(max_length=12)
    email = models.EmailField()
    address = models.TextField()
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    posi = (('save', "Savings"), ('current', "Current"), ('salary', "Salary"))
    account_type = models.CharField(max_length=20,choices=posi,default="save")
    mater = (('debit',"DebitCard"),('credit',"CreditCard"),('check',"Checkbook"))
    materials = models.CharField(max_length=20,choices=mater,default="debit")

    def __str__(self):
        return self.name