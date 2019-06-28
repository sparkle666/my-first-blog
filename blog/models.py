from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.

class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
	title = models.CharField(max_length=200)
	body = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

class Musician(models.Model):
	GENDER = [
		['M', 'Male'],
		['F', 'Female']
	]
	RATING = [
		[1, 1], 
		[2, 2],
		[3, 3],
		[4, 4],
		[5, 5],
		[6, 6],
		[7, 7],
		[8, 8],
		[9, 9],
		[10, 10]
	]
	stage_name = models.CharField(max_length=100)
	rating = models.IntegerField(choices=RATING)
	gender = models.CharField(max_length=1, choices=GENDER)

	def __str__(self):
		return self.stage_name

	def add_rating(self, num):
		return num + self.rating

class Student(models.Model):
	name = models.CharField(max_length=100)
	reg_number = models.CharField(max_length=100)

	def __init__(self, name, reg_num):
		self.name = name
		self.reg_number = reg_num

	def __str__(self):
		return self.name

class Subject(models.Model):
	subject_name = models.CharField(max_length=100)
	student = models.ForeignKey(Student, on_delete= models.CASCADE)
	def __str__(self):
		return self.subject_name