from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class EmployeeModel(models.Model):
    Employee_Id = models.AutoField(primary_key=True)
    Employee_Name = models.CharField(max_length=50, null=False)
    Contact_Number = models.IntegerField()
    Emergency_Contact_Number = models.IntegerField()
    Address = models.TextField()
    Postion = models.CharField(max_length=250)
    DOB = models.DateField()
    Martial_status = models.BooleanField(default=False)
    Blood_Group = models.CharField(max_length=10)
    Job_Title = models.CharField(max_length=250)
    work_Location = models.CharField(max_length=250)
    Date_of_Joining = models.DateField(auto_now=True)
    Reporting_to = models.CharField(max_length=250)
    Linked_In = models.URLField(max_length=250)
    Profile_Picture = models.ImageField(upload_to='media/profile', blank=True)
    Email = models.EmailField(unique=True, null=False)
    Password = models.CharField(max_length=100)

    def _unicode_(self):
        return self.Employee_Name

    def _str_(self):
        return '{}'.format(self.Employee_Name)


class LeaveApplication(models.Model):
    user = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE)
    apply_date = models.DateField(
        auto_now=False, auto_now_add=True, editable=False)
    nature_of_leave = models.CharField(max_length=100)
    first_Day = models.DateField()
    last_Day = models.DateField()
    number_Of_Days = models.IntegerField()
    # pending,approved,rejected,cancelled
    status = models.CharField(max_length=12, default='pending')
    is_approved = models.BooleanField(default=False)