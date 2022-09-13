from django.db import models

class Lead(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['first_name']
        
    def __str__(self):
        return f'{self.first_name} {self.last_name}'