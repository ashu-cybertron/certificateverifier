from django.db import models

class Attendee(models.Model):
    def __str__(self):
        return self.attendee_name
    attendee_name = models.CharField(max_length=50)
    certificate_id = models.CharField(max_length=20, default='syed0python02134')
    event_name = models.CharField(max_length=100)
    event_date = models.DateField('Date of Event')


