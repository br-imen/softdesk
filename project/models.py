from django.db import models

from django.db import models
from user.models import User

class Project(models.Model):
    # Choices for the type of project
    BACKEND = 'backend'
    FRONTEND = 'frontend'
    IOS = 'ios'
    ANDROID = 'android'
    TYPE_CHOICES = [
        (BACKEND, 'Back-end'),
        (FRONTEND, 'Front-end'),
        (IOS, 'iOS'),
        (ANDROID, 'Android'),
    ]

    # Name of the project
    name = models.CharField(max_length=255)  
    # Description of the project
    description = models.TextField() 
    # Type of the project 
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)  
    # Author of the project
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authored_projects') 
    # Contributors to the project
    contributors = models.ManyToManyField(User, related_name='contributed_projects', blank=True)  
    # Time when the project was created
    time_created = models.DateTimeField(auto_now_add=True)  
