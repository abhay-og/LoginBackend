from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
    def create_user(self, email, Date_Of_Birth, Name, TermsAndConditions, ContactNumber, password=None, password2=None):
        if not email:
            raise ValueError('User must have an email address')
        
        user = self.model(
            email=self.normalize_email(email),
            Date_Of_Birth=Date_Of_Birth,
            Name=Name,
            TermsAndConditions=TermsAndConditions,
            ContactNumber=ContactNumber,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self, email, Date_Of_Birth, Name, TermsAndConditions, ContactNumber, password=None):
        
        user = self.create_user(email=email, password=password, Date_Of_Birth=Date_Of_Birth, Name=Name, TermsAndConditions=TermsAndConditions, ContactNumber=ContactNumber)
        user.is_admin = True
        user.save(using=self._db)
        return user





class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    Date_Of_Birth = models.DateField(default=None)
    Name=models.CharField(max_length=255,default='')
    TermsAndConditions=models.BooleanField(default=False)
    ContactNumber=models.CharField(max_length=12,default='')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['Date_Of_Birth','Name','TermsAndConditions','ContactNumber']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin