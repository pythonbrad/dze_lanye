#insert_in_database_django_datalang
import random
from data_lang.word import dict_word

#a utiliser dans django shell
def run(Language ,Theme, Question, Answer, Choice):
	theme_name = ""
	old_theme = ""
	counter = 0
	lang = input('language: ')
	if lang == 'all':
		_lang = [i for i in dict_word]
	else:
		if lang in dict_word:
			_lang = [lang]
		else:
			raise Exception("lang %s not found"%lang)
	for lang in _lang:
		print(lang)
		if Language.objects.filter(name=lang):
			print(lang+' '+'already exists')
		else:
			language = Language(name=lang)
			language.save()
			is_first_theme = 1
			for theme_name in dict_word[lang]['themes']:
				print('  ', theme_name)
				theme = Theme(
					name=theme_name,
					required=old_theme if not is_first_theme else '',
					tag='%s_%s'%(lang, counter)
				)
				old_theme = '%s_%s'%(lang, counter)
				counter += 1
				is_first_theme = 0
				theme.language=language
				theme.save()
				for k in dict_word[lang]['themes'][theme_name]:
					question = Question(question_text=k,theme=theme)
					question.save()
					answers = [dict_word[lang]['themes'][theme_name][k]]
					for k1 in dict_word[lang]['themes'][theme_name]:
						answer_text = dict_word[lang]['themes'][theme_name][k1]
						if k1 == k and not answer_text in answers:
							answers.append(answer_text)
					for answer_text in answers:
						Answer.objects.create(answer_text=answer_text,question=question)
						Choice.objects.create(choice_text=answer_text,question=question)
					for _i in range(5):
						_temp = [__v for __k,__v in dict_word[lang]['themes'][theme_name].items()]
						Choice.objects.create(choice_text=random.choice(_temp),question=question)
	print('Finish')
