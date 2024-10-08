from django.db import models

class About(models.Model):
    full_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    image1 = models.ImageField(upload_to='about/')
    image2 = models.ImageField(default='path_to_default_image.jpg')
    description = models.TextField()
    twitter = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)

    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name  # "return" ichki qatorda bo'lishi kerak


