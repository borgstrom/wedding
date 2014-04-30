'''Models for the RSVP application'''

from django.db import models


class Invitation(models.Model):
    '''
    Represents an invitation to the wedding
    '''
    name = models.CharField(
        max_length=128,
        help_text='An informal name for this invitation'
    )
    guests = models.IntegerField(
        help_text='The number of guests on this invitation'
    )
    responded = models.BooleanField(
        default=False,
        help_text='Has this invitation been responded to'
    )
    updated = models.DateTimeField(
        auto_now=True
    )


class Person(models.Model):
    '''
    Represents a person coming to the wedding
    '''
    invitation = models.ForeignKey(
        Invitation,
        related_name='people'
    )
    first_name = models.CharField(
        max_length=64
    )
    last_name = models.CharField(
        max_length=128
    )
    attending = models.BooleanField(
        default=True
    )
    dietary_restrictions = models.TextField(
        blank=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )
