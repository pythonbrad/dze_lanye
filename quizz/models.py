from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

# Create your models here.

class Language(models.Model):
	name = models.CharField(max_length=50, unique=True)

	def __str__(self):
		return self.name

class Theme(models.Model):
	name = models.CharField(max_length=50, unique=True)
	language = models.ForeignKey(Language, on_delete=models.CASCADE)
	tag = models.CharField(max_length=20, unique=True)
	level = models.PositiveIntegerField(default=0)
	#eg: "food cook item".split()
	required = models.TextField(blank=True)

	def __str__(self):
		return self.name
	def is_unlock(self, user):
		themes_passed = DataUser.objects.get(user=user).theme_passed.split()
		themes_requis = Theme.objects.get(name=self.name).required.split()
		for i in themes_requis:
			if i != '':
				if not i in themes_passed:
					return False
		return True

class Question(models.Model):
	question_text = models.CharField(max_length=100)
	theme = models.ForeignKey(Theme, on_delete=models.CASCADE)

	def __str__(self):
		return self.question_text


class Answer(models.Model):
	answer_text = models.CharField(max_length=100)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)

	def __str__(self):
		return self.answer_text

class Choice(models.Model):
	choice_text = models.CharField(max_length=100, blank=True)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)

	def __str__(self):
		return self.choice_text

class DataUser(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	language = models.ForeignKey(Language, on_delete=models.CASCADE)
	score = models.PositiveIntegerField(default=0)
	#eg: "food cook item".split()
	theme_valided = models.TextField(blank=True)
	#eg: "food cook item".split()
	theme_passed = models.TextField(blank=True)

	def __str__(self):
		return self.user.username

class Remark(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	remark_text = models.CharField(max_length=100)
	pub_date = models.DateTimeField(default=timezone.now, verbose_name='Publication date')
	is_visible = models.BooleanField(default=1)

	def __str__(self):
		return self.remark_text
	def is_recent(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1) <= timezone.now()
	is_recent.short_description = 'Is recent?'
	is_recent.boolean = True