from django.db import models

class Resume(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    skills = models.TextField()
    experience = models.TextField()
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.name