from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime


STYLISTS = (
    ('A', 'Annabelle'),
    ('C', 'Corey'),
    ('D', 'Devlin'),
    ('G', 'Giang'),
    ('S', 'Scott'),
)

SERVICES = [
    ('B', 'Blowout'),
    ('WCS', 'Womens Cut & Style'),
    ('WMC', 'Womens Master Cut & Style'),
    ('MCW', 'Mens Wash & Scissor Cut'),
    ('LMC', 'Lengthy Master Color'),
    ('BMC', 'Buzz Master Color'),
    ('F', 'Fix Your Face'),
    ('FF', 'Face First'),
]


# Create your models here.
    
# # SERVICES
# class Service(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     type = models.CharField(max_length=100)
#     description = models.TextField(max_length=250)
#     cost = models.IntegerField(default=0)

#     def __str__(self):
#         return self.name

# # STYLISTS
# class Stylist(models.Model):
#     name = models.CharField(max_length=100)
#     master = models.BooleanField(True)
#     def service_choices():
#         return [(service.id, service.type) for service in Service.objects.all()]
#     services = models.ForeignKey(Service, on_delete=models.CASCADE, choices=service_choices,
#     max_length=8,
#     default=0
#     )
    

    # parent_service = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    # def __str__(self):
    #     return f"{self.get_stylists_display()}"

    # def get_absolute_url(self):
    #     return reverse('service-detail', kwargs={'pk': self.id})




# APPOINTMENTS
class Appointment(models.Model):
    date = models.DateField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.CharField(choices=SERVICES)
    stylist = models.CharField(choices=STYLISTS)

    def __str__(self):
        return f"{self.get_service_display()} on {self.date}"

    
    class Meta:
        ordering = ['-date']



# POST DATA
#  {date: 1/2/23, user: whatever, service: B, stylist: A }