from django.db import models
from django.db.models.functions import Now


class Participant(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_default=Now())
    fname = models.CharField(verbose_name="First Name", max_length=50)
    lname = models.CharField(verbose_name="Last Name", max_length=50)
    email = models.EmailField(max_length=255)
    phone = models.CharField(verbose_name="Phone No.", max_length=10)
    alt_phone = models.CharField(
        verbose_name="Alternate Phone No.", max_length=10, null=True
    )
    curr_year = models.PositiveSmallIntegerField(verbose_name="Current Year")
    university = models.CharField(max_length=255)
    address = models.TextField(max_length=300)
    pincode = models.CharField(max_length=10)
    state = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.f_name} {self.l_name}  |  {self.university}"


class Team(models.Model):
    class Designation(models.TextChoices):
        PROF = "PF", "Professor In Charge"
        MANAGER = "MG", "Manager"
        CORDINATOR = "CO", "Coordinator"

    # Fields
    created_at = models.DateTimeField(auto_now_add=True, db_default=Now())
    fullname = models.CharField(max_length=150)
    designation = models.CharField(
        max_length=2, choices=Designation, default=Designation.CORDINATOR
    )
    role = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    img_url = models.CharField(max_length=300)
    linkedin = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.fullname} | {self.Designation(self.designation).label}"

    def get_designation(self):
        return self.Designation(self.designation).label

    def is_prof(self):
        return self.designation == self.Designation.PROF

    def is_manager(self):
        return self.designation == self.Designation.MANAGER

    def is_coordinator(self):
        return self.designation == self.Designation.CORDINATOR

    def get_img_url(self):
        return f"imgs/team/{self.img_url}"
