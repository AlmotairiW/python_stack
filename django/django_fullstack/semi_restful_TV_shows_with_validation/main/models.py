from django.db import models
import time

class ShowManager(models.Manager):
    def show_validator(self, postData):
        # print(time.strptime(postData['rdate'], "%Y-%m-%d"))
        # print(time.localtime())
        errors = {}
        if len(postData["title"]) < 2:
            errors['title'] = "Title must be at least 2 characters long"
        if Show.objects.filter(title = postData['title']).exists():
            errors['title'] = "The show is already exists in the list of shows, enter a different one"
        if len(postData['network']) < 3:
            errors['network'] = "Network must be at least 3 characters long"
        if len(postData['desc']) != 0:
            if len(postData['desc']) < 10:
                errors['desc'] = "Description must be at least 10 characters long"
        if postData['rdate'] == "":
            errors['rdate'] = "Please choose a date"
        elif time.strptime(postData['rdate'], "%Y-%m-%d") > time.localtime():
            errors['rdate'] = "Release date must be in the past"
        return errors

class Show(models.Model):
    title = models.CharField(max_length = 255)
    network = models.CharField(max_length = 45)
    release_date = models.DateTimeField()
    description = models.TextField()
    objects = ShowManager()
    
    # Time/Date Stamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
