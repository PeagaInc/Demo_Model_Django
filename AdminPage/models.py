from django.db import models
from django.contrib.auth.models import User
from django.db.models import Max

# Create your models here.


class Persion(models.Model):
    persion_id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    user = models.OneToOneField(
        User, related_name="user_id", on_delete=models.DO_NOTHING)

    @property
    def sid(self):
        return "ST%06d" % self.persion_id

    def __str__(self):
        return str(self.persion_id)


class Human(models.Model):
    human_id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    user = models.OneToOneField(
        User, related_name="human_id", on_delete=models.PROTECT)

    @property
    def sid(self):
        return "ST%06d" % self.human_id

