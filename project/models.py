from django.db import models
from django.contrib.auth.models import User
# from import_export import resources
# from django.db.models.signals import post_save, post_delete
# from django.dispatch import receiver
from datetime import datetime, timezone


# Create your models here.

# class Services(resources.ModelResource):
#    course = [
#       ("CSC 315", "CSC 315"),
#       ("CSC 317", "CSC 317")
#    ] 

#    days_ = [
#      ("30mins", "30mins"),
#      ("1hr", "1hr"),
#      ("1 day", "24hrs"),
#      ("2 days", "48hrs")
#    ]

#    id = models.AutoField(primary_key=True)
#    Username = models.OneToOneField(User, on_delete=models.CASCADE, unique= True)
# #    option = models.FieldFile(max_length = 300)
   
#    date_created = models.DateTimeField(auto_now_add=True)
#    time = models.DateTimeField(null=True, blank = True)
#    Course_Code = models.CharField(choices=course, max_length=20, null=False)
#    Duration_Period = models.CharField(choices=days_, max_length = 20, null=False)
# #    deletion_time = datetime.now()-timedelta(days=days_)




#    file = models.FileField(upload_to= 'uploads/')

#    def __str__(self):
#     return f'{self.id}--{self.course}'

# class Record(models.Model):
# #     course = [
# #       ("CSC 315", "CSC 315"),
# #       ("CSC 317", "CSC 317")
# #    ] 

# #     days_ = [
# #      ("30mins", "30mins"),
# #      ("1hr", "1hr"),
# #      ("1 day", "24hrs"),
# #      ("2 days", "48hrs")
# #    ]


#     id = models.AutoField(primary_key=True)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     username = models.CharField(max_length=20)
#     matric_number = models.CharField(max_length=20)
#     email = models.CharField(max_length=300)
#     phone = models.CharField(max_length=20)
#     password= models.CharField(max_length=20, null=True)
#     creation_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.first_name+"   "+self.last_name
    
class user(models.Model):
    course = [
      ("CSC 315", "CSC 315"),
      ("CSC 317", "CSC 317")
   ] 
    
    status = [
      ("poor", "poor"),
      ("weak", "weak"),
      ("fair", "fair"),
      ("strong", "strong")
   ] 
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    matric_number = models.CharField(max_length=20)
    course = models.CharField(choices=course, max_length=20, null=False)
    score = models.CharField(max_length=10)
    status = models.CharField(choices=status, max_length=10, null=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.first_name+"   "+self.last_name
    


