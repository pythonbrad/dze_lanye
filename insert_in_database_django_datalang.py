import random
from word import dict_word

#faire le multi choix avec les mot qui reveienne plusieur fois

#a utiliser dans django shell
def run(Language ,Theme, Question, Answer, Choice):
	theme_id = 0
	theme_name = 0
	old_theme_id = -1
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
			theme_name = 1
			for key, value in dict_word[lang]['lang'].items():
				theme_id += 1
				if int(theme_id/10) != old_theme_id:
					old_theme_id = int(theme_id/10)
					print('  ', theme_name)
					theme = Theme(
						name='%s word %s'%(lang, theme_name),
						required='%s_%s'%(lang, old_theme_id) if not is_first_theme else '',
						tag='%s_%s'%(lang, old_theme_id+1)
					)
					is_first_theme = 0
					theme.language=language
					theme.save()
					theme_name += 1
				question = Question(question_text=value,theme=theme)
				question.save()
				answers = [dict_word[lang]['mlang'][key]]
				for _key, _value in dict_word[lang]['lang'].items():
					answer_text = dict_word[lang]['mlang'][_key]
					if _value == value and not answer_text in answers:
						answers.append(answer_text)
				for answer_text in answers:
					Answer.objects.create(answer_text=answer_text,question=question)
					Choice.objects.create(choice_text=answer_text,question=question)
				for _i in range(5):
					Choice.objects.create(choice_text=random.choice(dict_word[lang]['mlang']),question=question)

