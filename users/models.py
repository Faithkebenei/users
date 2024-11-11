from django.db import models

class User(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField(max_length=500)
    role = models.IntegerField()
    password = models.CharField(max_length=500)

    def __str__(self):
        return str(self.role) + ' ' + self.name + ' ' + self.email + ' ' + self.password
