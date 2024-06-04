from django.db import models

class Participant(models.Model):

    REGISTRATION_TYPES = [
        ('Virtual', 'Virtual'),
        ('Onsite', 'Onsite'),
    ]
    
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    registration_type = models.CharField(
        max_length=10,
        choices=REGISTRATION_TYPES
    )

    def __str__(self):
        return self.name


