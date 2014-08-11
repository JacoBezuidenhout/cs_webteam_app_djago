from django.db import models

# Create your models here.


class category(models.Model):
	text = models.TextField()

	def __str__(self):
		return self.text


class comment(models.Model):
	text = models.TextField()
# 	User??

class post(models.Model):
	title = models.TextField()
	body = models.TextField()
	date = models.DateField()
	category = models.ForeignKey(category)

	def __str__(self):
		return self.title

# User>>>