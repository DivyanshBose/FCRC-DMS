from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EmployeeDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.user.username


class Component(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    srNo = models.CharField(max_length=50, null=True)
    work = models.CharField(max_length=50, null=True)
    group = models.CharField(max_length=50, null=True)
    nmc = models.CharField(max_length=100, null=True)
    indate = models.DateField(max_length=50, null=True)
    outdate = models.DateField(max_length=50, null=True)
    servicableber = models.CharField(max_length=50, null=True)
    fault = models.CharField(max_length=50, null=True)
    doc = models.DateField(max_length=50, null=True)
    doj = models.DateField(max_length=50, null=True)
    remarks = models.CharField(max_length=50, null=True)
    info = models.CharField(max_length=50, null=True)

    def __str__(self) -> str:
        return self.user.username




