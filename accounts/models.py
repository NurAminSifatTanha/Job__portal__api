from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import PermissionsMixin


class CustomUserManager(BaseUserManager):
    """custom user email where email is unique.
    We can also pass Full name , email and password here"""

    def create_user(self, email, password, **extra_fields):
        """Create and save a User given email and password"""
        if not email:
            raise ValueError(_("The Email is must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """Create and save Super user with given email address"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Supperuser must have is_staff=True"))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Supperuser must have is_superuser=True"))

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(_('email_address'), unique=True)

    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    is_owner = models.BooleanField(default=False)
    is_seeker = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email


class Profile(models.Model):
    pro_photo = models.FileField(upload_to='media/profile',null=True,blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    degree_name = models.CharField(max_length=200,default='')
    graduate_year = models.CharField(max_length=200,default='')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    mother_name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField( max_length=8)
    religion = models.CharField(max_length=50)
    marital_status = models.CharField(max_length=50, blank=True, null=True)
    nationality = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    job_name = models.CharField(max_length=100, blank=True, null=True,default="")
    keywords = models.CharField(max_length=100,blank=True,null=True,default='')
    job_type = models.CharField(max_length=100,blank=True,null=True,default='')
    salary_range = models.CharField(max_length=100,blank=True,null=True,default='')
    created_at = models.DateTimeField(auto_now_add=True)
    resume = models.FileField(upload_to='resume/',null=True,blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class CompanyOwner(models.Model):
    user = models.ForeignKey(User,related_name="companies",on_delete=models.CASCADE)
    photo = models.FileField(upload_to='media/company/',null=True,blank=True)
    name = models.CharField(max_length=1000)
    company_logo = models.FileField(upload_to='company',null=True,blank=True)
    details = models.TextField(max_length=1000)
    locations = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.name

