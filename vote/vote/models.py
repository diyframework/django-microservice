from djongo import models
from question.models import Question

class Vote(models.Model):
	question_choice = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
	date_updated = models.DateTimeField(auto_now_add=True)