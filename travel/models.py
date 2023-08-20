from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=123)
    iata_code = models.CharField(max_length=4)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField(max_length=123)
    star_rate = models.PositiveIntegerField(default=0)
    amenity_group = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Order(models.Model):
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    order_date = models.DateField()
    name = models.CharField(max_length=123)
    last_name = models.CharField(max_length=123)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
