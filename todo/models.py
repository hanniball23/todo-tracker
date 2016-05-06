from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Post(models.Model):
	text = models.CharField(max_length = 160)
	deadline = models.DateField()
	progress = models.PositiveIntegerField(primary_key=True, validators=[MaxValueValidator(100)])

	def __str__(self):
		return self.text