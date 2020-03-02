from django.db import models

# Create your models here.

class Category(models.Model) :
    name = models.CharField(max_length=50,null=True,blank=True)
    total_post = models.IntegerField()

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.TextField()
    content = models.TextField()
    image = models.CharField(max_length=255,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)

    def __str__(self):
            return self.title
    pass

