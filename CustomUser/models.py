from django.db import models
from django.contrib.auth.models import AbstractUser
from Quiz.models import Quiz

class CustomUser(AbstractUser):
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username

class Quiz(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)


