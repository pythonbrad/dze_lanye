from django.shortcuts import render
from django.http import HttpResponse
from quizz.models import Question

# Create your views here.
def index_view(request):
	if 'word' in request.POST:
		word= request.POST['word']
		data = []
		temp = []
		for i in Question.objects.filter(question_text=word.capitalize()):
			if not i.theme.language in temp:
				data.append(i)
				temp.append(i.theme.language)
	else:
		data = []
	return render(request, 'mala/index.html', locals())