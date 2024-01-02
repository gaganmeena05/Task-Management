from django.db import models

class Task(models.Model):
    priority_choices = [
        (0, 'Low'),
        (1, 'Medium'),
        (2, 'High'),
    ]
    status_choices = [
        (False, 'Incomplete'),
        (True, 'Complete'),
    ]
    
    title = models.CharField(max_length=200,default = '')
    description = models.TextField(max_length=500,blank=False,null=False)
    status = models.BooleanField(choices = status_choices,default=False)
    priority = models.IntegerField(choices = priority_choices ,default=0)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.title:
            self.title = self.description[0:10]
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.description