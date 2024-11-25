from django.db import models

class Musician(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	birth = models.DateField()

	def __str__(self):
		return f"Musician(id={self.id}, last_name={self.last_name})"
	
class Venue(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return f"Venue(id={self.id}, name={self.name})"


class Room(models.Model):
	name = models.CharField(max_length=20)
	venue = models.ForeignKey(Venue, on_delete=models.CASCADE)  #1

	def __str__(self):
		return f"Room(id={self.id}, name={self.name})"