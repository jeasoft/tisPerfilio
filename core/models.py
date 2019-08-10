from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class CaseInsensitiveUserManager(UserManager):
    def get_by_natural_key(self, username):
        case_insensitive_username_field = '{}__iexact'.format(
            self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: username})


class User(AbstractUser):
    description = models.TextField()
    objects = CaseInsensitiveUserManager()

    def __str__(self):
        return self.username

class AuditModel(models.Model):
    class Meta:
        abstract = True

    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    created_date = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name


MONTH_CHOICES = (
    (1, "Enero"),
    (2, "Febrero"),
    (3, "Marzo"),
    (4, "Abril"),
    (5, "Mayo"),
    (6, "Junio"),
    (7, "Julio"),
    (8, "Agosto"),
    (9, "Septiembre"),
    (10, "Octubre"),
    (11, "Noviembre"),
    (12, "Diciembre"),
)


class Experience(AuditModel):
    class Meta:
        db_table = "user_experiences"

    company_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    job_description = models.TextField()
    year_starts = models.PositiveSmallIntegerField()
    month_starts = models.PositiveSmallIntegerField(choices=MONTH_CHOICES)
    year_ends = models.PositiveSmallIntegerField(blank=True, null=True)
    month_ends = models.PositiveSmallIntegerField(
        choices=MONTH_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.company_name


class Education(AuditModel):
    class Meta:
        db_table = "user_education"

    institution = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    year_starts = models.PositiveSmallIntegerField()
    month_starts = models.PositiveSmallIntegerField(choices=MONTH_CHOICES)
    year_ends = models.PositiveSmallIntegerField(blank=True, null=True)
    month_ends = models.PositiveSmallIntegerField(
        choices=MONTH_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.company_name

class Certification(AuditModel):
    class Meta:
        db_table = "user_certifications"

    certification_name = models.CharField(max_length=255)
    certification_institution = models.CharField(max_length=255)
    years = models.PositiveSmallIntegerField(blank=True, null=True)
    month = models.PositiveSmallIntegerField(
        choices=MONTH_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.certification_name
    