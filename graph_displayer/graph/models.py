from django.db import models

class Post(models.Model):
    count = models.IntegerField()
    
    def __str__(self):
        return self.count