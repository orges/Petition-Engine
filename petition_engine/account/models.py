from django.db import models
from django.contrib.auth.models import User,Group
from taggit.managers import TaggableManager


class Account(User):

    # keep interests of this account
    tags = TaggableManager()
    organizations = models.ManyToManyField('Organization')


class Organization(Group):

    # keep topics that organization deals with
    tags = TaggableManager()
    core_team = models.ManyToManyField(Account)
