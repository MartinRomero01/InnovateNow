from django.db import models

class NavbarItem(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='services/', blank=True, null=True)


    def __str__(self):
        return self.title
