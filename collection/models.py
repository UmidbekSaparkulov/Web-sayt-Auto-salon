from django.db import models

class Collection(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='collection/')

    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    
