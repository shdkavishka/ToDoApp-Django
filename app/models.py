from django.db import models

# Create your models here.

class Task(models.Model):
    taskTitle = models.CharField(max_length=30)#smallcharacters
    taskDesc = models.TextField(max_length=300)#big amount of charatctors
    time = models.DateTimeField(auto_now_add=True)#Time will actual updated
    
    #to show topic as My Task Title in admin panel
    def __str__(self):
        return self.taskTitle