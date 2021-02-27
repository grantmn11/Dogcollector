from django.db import models
from django.urls import reverse

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)
# Create your models here.

# from django.urls import reverse

# Create your models here.
class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'toy_id': self.id})

class Dog(models.Model):
    name = models.CharField(max_length=150)
    breed = models.CharField(max_length=150)
    description = models.TextField(max_length=150)
    age = models.IntegerField()
    toys = models.ManyToManyField(Toy)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('dogs_detail', kwargs={'dogs_id': self.id})

class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1, 
        choices = MEALS,
        default = MEALS[0][0]
        )

    # this will become cat_id
    # one cat has many feedings
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_meal_display()} at {self.date}'

    class Meta:
        ordering = ['-date']
    