from django.db import models

# Create your models here.
class spentAmount(models.Model):
    Title =models.CharField(max_length=100)
    Date =models.DateField()
    Amount = models.DecimalField(max_digits=10,decimal_places=2)
    Description =models.TextField(blank=True,null=True)
    
    def __str__(self):
       return self.Title