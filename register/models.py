from django.db import models
from django.contrib.auth.models import (
    AbstractUser,BaseUserManager
)
# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email,first_name,last_name,school_name,gender,adhaar_card,city,country,mother_name,father_name,mobile_number,address,date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            first_name=first_name,
            last_name=last_name,
            school_name=school_name,
            gender=gender,
            adhaar_card=adhaar_card,
            city=city,
            country=country,
            mother_name=mother_name,
            father_name=father_name,
            mobile_number=mobile_number,
            address=address,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,first_name,last_name,school_name,gender,adhaar_card,city,country,mother_name,father_name,mobile_number,address, date_of_birth, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            
            date_of_birth=date_of_birth,
            first_name=first_name,
            last_name=last_name,
            school_name=school_name,
            gender=gender,
            adhaar_card=adhaar_card,
            city=city,
            password=password,
            country=country,
            mother_name=mother_name,
            father_name=father_name,
            mobile_number=mobile_number,
            address=address,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class  MyUser(AbstractUser):

    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)

    school_name = models.CharField(max_length=500)
    gender = models.CharField(max_length=6)

    date_of_birth= models.DateTimeField()
    adhaar_card = models.IntegerField()
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    mobile_number = models.IntegerField()
    email = models.EmailField(max_length=50,unique=True)
    address = models.CharField(max_length=500)
    is_active  = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth',"first_name","last_name","school_name","gender","adhaar_card",
                       "city","country","mother_name","father_name","mobile_number","address",

                       ]


    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin










