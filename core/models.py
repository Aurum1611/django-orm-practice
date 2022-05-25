from django.db import models
from django.contrib.auth.models import User


class State(models.Model):
    name = models.CharField(max_length=50)
    code = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50)
    code = models.IntegerField()
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class College(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    phone_num = models.CharField(max_length=10)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class ElectiveSubject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField()
    email = models.EmailField()
    phone_num = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    elective = models.ManyToManyField(ElectiveSubject)

    def __str__(self) -> str:
        return self.name
