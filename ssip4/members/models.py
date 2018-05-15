from django.db import models

class Member(models.Model):
    # basic information
    first_name = models.CharField(max_length=200, null=False, blank=False)
    last_name = models.CharField(max_length=200, null=False, blank=False)
    birthday = models.CharField(max_length=200, null=True, blank=True)

    # contact information
    town = models.CharField(max_length=400, null=True, blank=True)
    address = models.CharField(max_length=400, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    homephone = models.CharField(max_length=200, null=True, blank=True)
    cellphone = models.CharField(max_length=200, null=True, blank=True)

    # emergency contact
    emergency_first_name = models.CharField(max_length=200, null=True, blank=True, default=None)
    emergency_last_name = models.CharField(max_length=200, null=True, blank=True, default=None)
    emergency_homephone = models.CharField(max_length=200, null=True, blank=True, default=None)
    emergency_cellphone = models.CharField(max_length=200, null=True, blank=True, default=None)
    emergency_comment = models.TextField(max_length=500, null=True, blank=True, default=None)

    # preferences
    hobbies = models.CharField(max_length=1500, null=True, blank=True)
    canhelp = models.CharField(max_length=1500, null=True, blank=True)
    needhelp = models.CharField(max_length=1500, null=True, blank=True)
    comments = models.TextField(max_length=5000, null=True, blank=True)

    # picture
    picture = models.ImageField(upload_to='members/', null=True, default=None)

    def get_full_name(self):
        return " ".join([self.first_name, self.last_name])

    def __str__(self):
        return self.get_full_name()

    class Meta:
        ordering = ['last_name']