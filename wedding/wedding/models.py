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
    responded = models.BooleanField(
        default=False,
        help_text='Has this invitation been responded to'
    )
    updated = models.DateTimeField(
        auto_now=True
    )

    @property
    def guests(self):
        return self.people.filter(attending=True).count()


class Person(models.Model):
    '''
    Represents a person coming to the wedding
    '''
    invitation = models.ForeignKey(
        Invitation,
        related_name='people'
    )
    first_name = models.CharField(
        max_length=64,
        blank=True
    )
    last_name = models.CharField(
        max_length=128,
        blank=True
    )
    attending = models.NullBooleanField(
        blank=True,
        null=True
    )
    dietary_restrictions = models.TextField(
        blank=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )
