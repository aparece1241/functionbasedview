from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username

class Quiz(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	quiz_id = models.ForeignKey('Quiz.Quiz', related_name='user_quiz' , on_delete=models.CASCADE)


