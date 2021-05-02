from django.db import models
import re
from datetime import date
import datetime
import time
class UserManager(models.Manager):

    def reg_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9_-]+\.[a-zA-Z]+$')

        if len(postData['fname']) < 2:
            errors['fname'] = "First Name should be at least 2 characters long"
        if len(postData['lname']) < 2:
            errors['lname'] = "Last Name should be at least 2 characters long"

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid e-mail address!"
        elif User.objects.filter(email = postData['email']).exists():
            errors['email'] = "The email is already registered! go to log in :)"

        if len(postData['pass']) < 8:
            errors['pass'] = "Password should be at least 8 charachters long"
        if postData['pass'] != postData['pass_c']:
            errors['pass_c'] = "Password does not match!"
        
        return errors
        
    def login_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9_-]+\.[a-zA-Z]+$')

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid e-mail address!"
        elif not User.objects.filter(email = postData['email']).exists():
            errors['email'] = "The email is not registered! go to registeration :)"
        if len(postData['pass']) < 8:
            errors['pass'] = "Password should be at least 8 charachters long"
    
        return errors

class BookManager(models.Manager):
    def book_validator(self, postData):
        errors = {}

        if postData['title'] == "":
            errors['title'] = "Title is required!"
        if len(postData['desc']) < 5:
            errors['desc'] = "Description must be at least 5 Characters long!"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email = models.CharField(max_length = 50)
    password =  models.CharField(max_length = 50)
    objects = UserManager()

    #date & time stamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length = 255)
    desc = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name = "books_uploaded", on_delete= models.CASCADE)
    users_who_like = models.ManyToManyField(User, related_name = "liked_books")
    objects = BookManager()

    #date & time stamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
