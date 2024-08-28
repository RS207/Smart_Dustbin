from django.db import models





# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    country_code = models.CharField(max_length=3)
    contact_number = models.CharField(max_length=20)
    desc = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.date.date()})"