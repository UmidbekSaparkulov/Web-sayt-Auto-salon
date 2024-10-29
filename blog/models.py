from django.db import models
from django.utils import timezone

class  Category(models.Model):
    company = models.CharField(max_length=200)
    def __str__(self):
         return self.company



class Tag(models.Model):

    engineer = models.CharField(max_length=200)

    def __str__(self):
        return self.engineer


class Blog(models.Model):
    make = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    image = models.ImageField(upload_to='blog/') 
    tags = models.ManyToManyField(Tag, )
    content = models.TextField()
    content2 = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"


class Comment(models.Model):

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comment')
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    message = models.TextField()

    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class Subscribe(models.Model):
    email = models.EmailField()


    is_published = models.BooleanField(default=False)
    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.email