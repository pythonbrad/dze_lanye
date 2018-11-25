import random
from django.conf import settings

def theme_full(data, theme, full=True):
	#it's id
	tag = str(theme.tag)
	if full:
		_ = data.theme_valided.split()
	else:
		_ = data.theme_passed.split()
	if not tag in _:
		_.append(tag)
		t = ''
		for tag in _:
			t += ' '+tag
		if full:
			data.theme_valided = t
		else:
			data.theme_passed = t
		data.save()

def mysort(x):
	_ = []
	while len(x) != len(_) :
		e=random.choice(x)
		if not e in _:
			_.append(e)
	return _