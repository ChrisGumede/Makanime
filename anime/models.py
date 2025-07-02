from django.db import models
from datetime import timedelta  
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

# Create your models here.
class AnimeCatalog(models.Model): 
      
    title = models.CharField(max_length=200)
    overview = models.TextField(blank=True)
    type = models.CharField(max_length=100)  
    studio = models.CharField(max_length=100)
    aired = models.DateField(default=timezone.now)
    status = models.CharField(max_length=100)  
    genre = models.CharField(max_length=100, default="Action")
    premiered = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField(default=timedelta(minutes=24))
    views = models.PositiveIntegerField(default=0)
    image = models.CharField(max_length=300)
    score = models.FloatField(
    default=0.0,  
    validators=[
        MinValueValidator(0.0),  
        MaxValueValidator(10.0)  
    ]
)
    quality = models.CharField(
    max_length=100,
    default="HD",
    choices=[
        ('HD', 'High Definition'),
        ('SD', 'Standard Definition'),
        ('4K', 'Ultra HD')
    ]
) 
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-premiered']