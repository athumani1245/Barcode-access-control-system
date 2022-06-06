from audioop import reverse
from tabnanny import verbose
from django.db import models


class Location(models.Model):
    venue_name = models.CharField(max_length = 50)
    capacity = models.IntegerField()
    ip_enter = models.CharField(max_length = 50,null = True)
    ip_leave = models.CharField(max_length = 50, null = True)

    
    def get_url(self):
        return reverse('venue_name')
    def __str__(self):
        return self.venue_name
    
    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'
    

def pool_giver():
    info = Location.objects.get(venue_name = "Pool")
    value = info.id
    return value



class People(models.Model):
    rank = (
        ('1', 'Students'),
        ('2', 'Staffs'),
        ('3', 'Visitors')
    )
    occupation = models.CharField(max_length=8, default='Students', choices=rank)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    personal_id = models.CharField(max_length=100)
    venue_name = models.ForeignKey(Location, on_delete = models.CASCADE,default = pool_giver)

    def __str__(self):
        return self.personal_id
    
    class Meta:
        verbose_name = 'person'
        verbose_name_plural = 'people'


class Custodian(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=40)
    custodian_id = models.CharField(max_length=20)
    username = models.CharField(max_length=20, default=first_name)
    password = models.CharField(max_length=35)

    def __str__(self):
        return self.custodian_id
    
    class Meta:
        verbose_name = 'Custodian'
        verbose_name_plural = 'Custodians'


class Record(models.Model):
    record_id = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)
    venue_name = models.CharField(max_length = 50, null=True)
    today_date=models.DateField(null=True)
    time_in = models.TimeField(null=True)
    time_out = models.TimeField(null=True)

    def __str__(self):
        return self.record_id
    
    class Meta:
        verbose_name = 'Record'
        verbose_name_plural = 'Records'
