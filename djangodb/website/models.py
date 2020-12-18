from django.db import models

class Member(models.Model):
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    passwd = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.fname + ' ' + self.lname + ' ' + self.email
