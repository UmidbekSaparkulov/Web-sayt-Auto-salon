from django.db import models

class  Category(models.Model):

    title = models.CharField(max_length=200)


    def __str__(self):
        return self.title



class Tag(models.Model):

    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Blog(models.Model):

    title = models.CharField(max_length=200)
    categroy = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    body_one = models.TextField()
    image = models.ImageField(upload_to='blog/')
    body_two = models.TextField()
    tags = models.ManyToManyField(Tag, )

    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


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

