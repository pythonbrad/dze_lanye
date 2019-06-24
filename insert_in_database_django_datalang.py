from quizz.models import *
from data_lang.word import dict_word
import random
from django.contrib.auth.models import User

def run(Language ,Theme, Question, Answer, Choice):
	language = input('Language: ').split(',')
	if not language or language == ['all']:
		language = [i for i in dict_word]
	print(language, 'to inserted')
	for lang in language:
		i = 0
		print(lang)
		if not Language.objects.filter(name=lang):
			_lang = Language(name=lang)
			_lang.save()
			for theme in dict_word[lang]:
				print('  theme')
				_theme = Theme()
				_theme.name = theme
				_theme.language = _lang
				_theme_has_formated = "{}_theme_%s".format(lang)
				_theme.tag = _theme_has_formated%i
				#if i != 0:
				#	_theme.required = _theme_has_formated%(i-1)
				_theme.save()
				i += 1
				for word_id in dict_word[lang][theme]['lang']:
					print('    question')
					question = Question()
					question.question_text = dict_word[lang][theme]['lang'][word_id]
					question.theme = _theme
					question.save()
					_temp = []
					for _word_id in dict_word[lang][theme]['mlang']:
						_word_id_lang = dict_word[lang][theme]['lang'][_word_id]
						_answer = dict_word[lang][theme]['mlang'][_word_id]
						if question.question_text == _word_id_lang:
							print('      answer')
							answer = Answer()
							answer.answer_text = _answer
							answer.question = question
							answer.save()
							choice = Choice()
							choice.choice_text = _answer
							choice.question = question
							choice.save()
						_temp.append(_answer)
					for _i in range(5):
						print('        choice')
						_choice = random.choice(_temp)
						if not Choice.objects.filter(choice_text=_choice, question=question):
							choice = Choice()
							choice.choice_text = _choice
							choice.question = question
							choice.save()


user = User(username='admin', password='adminroottoor')
user.is_staff = True
user.is_superuser = True
user.save()

print('superuser created wth username <admin> and password <adminroottoor>')
