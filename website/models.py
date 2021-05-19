from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.forms import DateField, CharField, ChoiceField, TextInput
from django.urls import reverse   


# Create your models here.

class Post(models.Model):
    Title= models.CharField(max_length=100000, default="")
    Synopsis= models.CharField(max_length=100000, default="")
    Judging= models.CharField(max_length=100000, default='-')
    Title_in_Original_Language= models.CharField(max_length=100000, default='-')
    Year_Submitted= models.CharField(max_length=100000, default='-')
    Duration= models.CharField(max_length=100000,  default='-')
    Category= models.CharField(max_length=100000, default='-')
    Language= models.CharField(max_length=100000, default="")
    Genre= models.CharField(max_length=100000, default="")
    Subtitles= models.CharField(max_length=100000, default="")
    Student_Project= models.CharField(max_length=100000, default="")
    Completion_Date= models.CharField(max_length=100000, default="")
    Submission_Name= models.CharField(max_length=100000, default="")
    Submission_email= models.CharField(max_length=100000, default="")
   	# Submission_Phone= models.CharField(max_length=100000, default="")
    Submission_City= models.CharField(max_length=100000, default="")
    Director_first_name= models.CharField(max_length=100000, default="")
    Director_email= models.CharField(max_length=100000, default="")
    Director_phone= models.CharField(max_length=100000, default="")
    Producer_first_name= models.CharField(max_length=100000, default="") 
    Producer_email= models.CharField(max_length=100000, default="")
	# Producer_Phone= models.CharField(max_length=100000, default="")
    Distributor_name= models.CharField(max_length=100000, default="")
    Distributor_phone= models.CharField(max_length=100000, default="")
    Distributor_email= models.CharField(max_length=100000, default="")
    Key_cast= models.CharField(max_length=100000, default="")
    Screenwriters= models.CharField(max_length=100000, default="")
    Composer_name= models.CharField(max_length=100000, default="")
    Cinematographer_name= models.CharField(max_length=100000, default="") 
    Rating= models.CharField(max_length=100000, default="")
    Production_budget= models.CharField(max_length=100000, default="")
    First_time_filmmakers= models.CharField(max_length=100000, default="")
    Physical_copy= models.CharField(max_length=100000, default="")
    Submission_Phone= models.CharField(max_length=100000, default="")
    Producer_Phone= models.CharField(max_length=100000, default="")




    def __str__(self):
        return self.Title

    def get_absolute_url(self):       
         return reverse('detail', args=[str(self.id)])




class Contact(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    subject = models.TextField(null=True)

    def __str__(self):
        return self.name