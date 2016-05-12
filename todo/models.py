from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Post(models.Model):
	text = models.CharField(max_length = 160, default='')
	deadline = models.DateField()
	progress = models.PositiveIntegerField(validators=[MaxValueValidator(100)],default=0)
	#id = models.AutoField(primary_key=True)

	def __str__(self):
		return self.text