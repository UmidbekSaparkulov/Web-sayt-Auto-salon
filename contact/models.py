from django.db import models

class Contact_info(models.Model):

    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    linkedin = models.CharField(max_length=100)

    def __str__(self):
        return self.phone



class Contact(models.Model):

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField()

    is_published = models.BooleanField(default=False)

    create_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
        
        
