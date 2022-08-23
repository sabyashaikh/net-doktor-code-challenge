from django.db import models

STATUS_CHOICES = (
    ("Created", "Created"),
    ("Archived", "Archived"),
    ("Booked", "Booked"),
)


class Campaign(models.Model):
    cs_id = models.BigAutoField(primary_key=True)
    customer = models.CharField(max_length=200, default="", blank=True)
    name = models.CharField(max_length=100, default="", blank=True)
    start = models.DateField(blank=True)
    end = models.DateField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="Created")
    note = models.CharField(max_length=200, default="", blank=True)

    def __str__(self):
        return str(self.cs_id) + ' ' + str(self.name)
