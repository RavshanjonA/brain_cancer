from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Model, CharField, IntegerField, BooleanField, ForeignKey, CASCADE, \
    PositiveSmallIntegerField


class Users(Model):
    first_name = CharField(max_length=124)
    last_name = CharField(max_length=124)
    age = PositiveSmallIntegerField()
    region = CharField(max_length=124)
    district = CharField(max_length=124)

    class Meta:
        verbose_name_plural = 'Users'

    def __str__(self):
        return "{}-{}".format(self.first_name, self.last_name)


class Params(Model):
    user = ForeignKey('apps.Users', on_delete=CASCADE, related_name='params')
    x2 = BooleanField()
    x6 = BooleanField()
    x11 = PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    x12 = PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    x18 = PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    x19 = PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])

    class Meta:
        verbose_name_plural = 'Params'

    def __str__(self):
        return "{}-{}".format(self.user.first_name, self.user.age)
