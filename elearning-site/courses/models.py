from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

User = get_user_model()

class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return self.title
    
class Course(models.Model):
    owner = models.ForeignKey(User, related_name='courses_created', on_delete=models.CASCADE)
    subject = 