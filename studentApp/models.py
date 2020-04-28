from django.test import TestCase
from django.db import models
from django.contrib.auth.decorators import login_required
from django.conf import settings
from model_utils import Choices


# Create your tests here.
from django.utils import timezone

# Create your models here.


class User(models.Model):
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    email = models.EmailField(max_length=64, unique=True)
    address_1 = models.PositiveIntegerField(default=0)
    address_2 = models.PositiveIntegerField(default=0)
    city = models.CharField(max_length=64, default="Nairobi")
    state = models.CharField(max_length=64, default="Kenya")
    zip_code = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now, editable=False)
    last_seen = models.DateTimeField(default=timezone.now)

    def get_id(self):
        return str(self.id)

    def __str__(self):
        return '<User(fullname={} {})>'.format(self.firstname, self.lastname)


class StudentProfile(models.Model):

    school_Choices = Choices('SELECT', 'Meru University', 'Other')
    sex_choice = Choices('SELECT', 'Male', 'Female')
    address_choice = Choices('SELECT', 'U', 'R')
    famsize_choice = Choices('SELECT', 'GT3', 'LT3')

    fedu_choice = Choices(0, 1, 2, 3, 4)
    medu_choice = Choices(0, 1, 2, 3, 4)
    fjob_choice = Choices('SELECT', 'home', 'health', 'services', 'other')
    mjob_choice = Choices('SELECT', 'home', 'health', 'services', 'other')
    reason_choice = Choices('SELECT', 'course', 'home', 'reputation', 'other')
    guardian_choice = Choices('SELECT', 'father', 'mother', 'other')
    traveltime_choice = Choices(1, 2, 3, 4)
    studytime_choice = Choices(1, 2, 3, 4)
    failures_choice = Choices(0, 1, 2, 3, 4)
    schoolsup_choice = Choices('SELECT', 'yes', 'no')
    famsup_choice = Choices('SELECT', 'yes', 'no')
    paid_choice = Choices('SELECT', 'yes', 'no')
    activities_choice = Choices('SELECT', 'yes', 'no')
    nursery_choice = Choices('SELECT', 'yes', 'no')
    higher_choice = Choices('SELECT', 'yes', 'no')
    internet_choice = Choices('SELECT', 'yes', 'no')
    romantic_choice = Choices('SELECT', 'yes', 'no')
    famrel_choice = Choices(1, 2, 3, 4, 5)
    freetime_choice = Choices(1, 2, 3, 4, 5)
    goout_choice = Choices(1, 2, 3, 4, 5)
    dalc_choice = Choices(1, 2, 3, 4, 5)
    walc_choice = Choices(1, 2, 3, 4, 5)
    health_choice = Choices(1, 2, 3, 4, 5)

    student_id = models.ForeignKey(
        'Student', on_delete=models.CASCADE, null=True)
    school = models.CharField(choices=school_Choices,
                              default=school_Choices.SELECT, max_length=64)
    sex = models.CharField(
        choices=sex_choice, default=sex_choice.SELECT, max_length=64)
    age = models.PositiveSmallIntegerField(null=True)
    address = models.CharField(
        choices=address_choice, default=address_choice.SELECT, max_length=64)
    famsize = models.CharField(
        choices=famsize_choice, default=famsize_choice.SELECT, max_length=64)

    fedu = models.PositiveIntegerField(
        choices=fedu_choice, default=0)
    medu = models.PositiveIntegerField(
        choices=medu_choice, default=0)
    mjob = models.CharField(choices=mjob_choice,
                            default=mjob_choice.SELECT, max_length=64)
    fjob = models.CharField(choices=fjob_choice,
                            default=fjob_choice.SELECT, max_length=64)
    reason = models.CharField(choices=reason_choice,
                              default=reason_choice.SELECT, max_length=64)
    guardian = models.CharField(choices=guardian_choice,
                                default=guardian_choice.SELECT, max_length=64)
    traveltime = models.PositiveIntegerField(choices=traveltime_choice,
                                             default=1)
    studytime = models.PositiveIntegerField(choices=studytime_choice,
                                            default=1)
    failures = models.PositiveIntegerField(choices=failures_choice,
                                           default=0)
    schoolsup = models.CharField(choices=schoolsup_choice,
                                 default=schoolsup_choice.SELECT, max_length=64)
    famsup = models.CharField(choices=famsup_choice,
                              default=famsup_choice.SELECT, max_length=64)
    paid = models.CharField(choices=paid_choice,
                            default=paid_choice.SELECT, max_length=64)
    activities = models.CharField(choices=activities_choice,
                                  default=activities_choice.SELECT, max_length=64)
    nursery = models.CharField(choices=nursery_choice,
                               default=nursery_choice.SELECT, max_length=64)
    higher = models.CharField(choices=higher_choice,
                              default=higher_choice.SELECT, max_length=64)
    internet = models.CharField(choices=internet_choice,
                                default=internet_choice.SELECT, max_length=64)
    romantic = models.CharField(choices=romantic_choice,
                                default=romantic_choice.SELECT, max_length=64)
    famrel = models.PositiveIntegerField(choices=famrel_choice,
                                         default=1)
    freetime = models.PositiveIntegerField(choices=freetime_choice,
                                           default=1)
    goout = models.PositiveIntegerField(choices=goout_choice,
                                        default=1)
    dalc = models.PositiveIntegerField(choices=dalc_choice,
                                       default=1)
    walc = models.PositiveIntegerField(choices=walc_choice,
                                       default=1)
    health = models.PositiveIntegerField(choices=health_choice,
                                         default=1)
    absences = models.PositiveIntegerField(default=0)

    def get_id(self):
        return str(self.id)

    def __str__(self):
        return '<Student(fullname={})>'.format(self.id)


class Student(models.Model):
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    email = models.EmailField(max_length=64, unique=True)
    address_1 = models.PositiveIntegerField(default=0)
    address_2 = models.PositiveIntegerField(default=0)
    city = models.CharField(max_length=64, default="Nairobi")
    state = models.CharField(max_length=64, default="Kenya")
    zip_code = models.PositiveIntegerField(default=1)
    created_date = models.DateTimeField(default=timezone.now)
    student_profile = models.ForeignKey(
        StudentProfile, on_delete=models.CASCADE, null=True)

    def get_id(self):
        return str(self.id)

    def __str__(self):
        return '<Student(fullname={} {})>'.format(self.firstname, self.lastname)


class UserFeedbackModel(models.Model):

    MY_CHOICES = (
        ('Verygood', '👍Verygood'),
        ('good', '👌awesome'),
        ('Average', '🙌average'),
        ('Bad', '😒poor'),

    )

    Rate_us = models.CharField(max_length=64, choices=MY_CHOICES, blank=True)

    comment = models.TextField()

    def __str__(self):

        return self.Rate_us
