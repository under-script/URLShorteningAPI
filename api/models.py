from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.db import models
from django_extensions.db.models import TimeStampedModel
import random
import string

from URLShorteningAPI import settings

User = get_user_model()

def validate_code_length(value):
    if len(value) != 8:
        raise ValidationError('The short_code must be exactly 8 characters long.')


def generate_unique_code():
    characters = string.ascii_letters + string.digits
    while True:
        code = ''.join(random.choices(characters, k=8))
        if not Shorten.objects.filter(short_code=code).exists():
            return code


class Shorten(TimeStampedModel):
    long_url = models.URLField(max_length=4000, unique=True)
    short_url = models.URLField(max_length=20, unique=True)
    short_code = models.CharField(
        max_length=8,  # Required by Django
        validators=[validate_code_length],  # Custom validator for exact length
        unique=True,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.short_url

    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = generate_unique_code()

        # Use the domain from settings
        domain = settings.SHORTEN_DOMAIN
        self.short_url = domain + self.short_code

        super().save(**kwargs)
