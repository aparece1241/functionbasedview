from django.db import models
from CustomUser.models import CustomUser

# Create your models here.

class Quiz(models.Model):

	class QuizStatus(models.TextChoices):
		DEACTIVATED = 'deactivated'
		ACTIVATED = 'activated'

	title = models.CharField(max_length=225)
	author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	code = models.CharField(max_length=100)
	limit = models.IntegerField()
	start_date = models.DateField(default=None)
	end_date = models.DateField(default=None)
	status = models.CharField(max_length=100,default=QuizStatus.DEACTIVATED, choices=QuizStatus.choices)
	instruction = models.TextField()

	def __str__(self):
		return self.title

class Question(models.Model):
	class QuestionType(models.TextChoices):
		MULTIPLECHOICE = 'multiple-choice'
		IDENTIFICTION = 'identification'
		TRUEORFALSE = 'true-or-false'
	question = models.TextField()
	type = models.CharField(default=None, choices=QuestionType.choices, max_length=50)
	points = models.IntegerField(default=1)
	answer = models.CharField(max_length=200)
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

	def __str__(self):
		return self.question

