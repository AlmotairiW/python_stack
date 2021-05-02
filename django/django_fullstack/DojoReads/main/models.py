from django.db import models
import re
from datetime import date
import datetime
import time
class UserManager(models.Manager):

    def reg_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9_-]+\.[a-zA-Z]+$')

        if len(postData['name']) < 2:
            errors['name'] = "Name should be at least 2 characters long"
        if len(postData['ali']) < 2:
            errors['ali'] = "Alias should be at least 2 characters long"

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
        if len(postData['title']) < 2:
            errors['title'] = "Title must be at least 2 character!"
        
        if postData['c_author'] == "-1":
            if len(postData['author']) < 2:
                errors['author'] = "Author name must be at least 2 charactors"

        if len(postData['rev']) < 4:
            errors['rev'] = "Review must be at least a 4 character"
        
        return errors

class User(models.Model):
    name = models.CharField(max_length = 45)
    alias = models.CharField(max_length = 45)
    email = models.CharField(max_length = 50)
    password =  models.CharField(max_length = 50)
    objects = UserManager()

    #date & time stamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    name = models.CharField(max_length = 45)
    #date & time stamps
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Book(models.Model):
    title = models.CharField(max_length = 255)
    added_by = models.ForeignKey(User, related_name = "books_added", on_delete= models.CASCADE)
    author = models.ForeignKey(Author, related_name = "books", on_delete = models.CASCADE)
    objects = BookManager()
    

    #date & time stamps
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Review(models.Model):
    review_txt = models.TextField()
    book = models.ForeignKey(Book, related_name = "reviews", on_delete = models.CASCADE)
    rating = models.IntegerField()
    user = models.ForeignKey(User, related_name = "reviews", on_delete = models.CASCADE)

    #date & time stamps
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
