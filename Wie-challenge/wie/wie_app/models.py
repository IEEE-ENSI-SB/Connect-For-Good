from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from ckeditor.fields import RichTextField

class CustomUser(AbstractUser):
    image = models.ImageField(default='../static/images/default_image.jpg', upload_to='images/', blank=True, null=True)
    email = models.EmailField(unique=True, blank=False, null=True)
    role = models.CharField(
        max_length=20,
        default='user',
        blank=False,
        null=False
    )
    phone = models.CharField(max_length=8, validators=[RegexValidator(r'^\d{8}$', message='Phone number must be 8 digits.')], blank=False, null=False)
    name = models.CharField(max_length=255, blank=False)  # Add the name field here

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


    def __str__(self):
        return self.username

class Donation(models.Model):
    fullName = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(max_length=200, blank=False, null=False)
    phone = models.CharField(max_length=8, validators=[RegexValidator(r'^\d{8}$', message='Phone number must be 8 digits.')], blank=False, null=False)
    Address = models.CharField(max_length=200, blank=False, null=False)
    Files = models.ImageField(default='../static/images/default_image.jpg', upload_to='images/', blank=True, null=True)

class Invitation(models.Model):
    date = models.DateTimeField()
    body = RichTextField(blank=True, null=True)
    participants = models.ManyToManyField(CustomUser, related_name='participants', blank=True)
    needs = models.TextField(blank=True, null=True, default='')

