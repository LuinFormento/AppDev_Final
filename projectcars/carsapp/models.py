from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Logo(BaseModel):
    logo_image = models.ImageField(upload_to='logo_images/', null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Classification(BaseModel):
    classification_name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.classification_name

class AutoOrSemi(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Car_Model(BaseModel):
    make = models.CharField(max_length=255)
    model = models.TextField(unique=True)
    year = models.TextField()
    logo = models.ForeignKey(Logo, on_delete=models.SET_NULL, null=True)
    classification = models.ForeignKey(Classification, on_delete=models.SET_NULL, null=True)
    autoorsemi = models.ManyToManyField(AutoOrSemi)

    def __str__(self):
        return f"{self.make} {self.model}"

class Vehicle(BaseModel):
    vehicle_image = models.ImageField(upload_to='vehicle_images/', null=True, blank=True)
    car = models.TextField(Car_Model)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.car