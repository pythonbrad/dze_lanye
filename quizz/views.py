from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse
from .models import Question, Choice, Theme, Comment, DataUser, Answer, Language
from .forms import SigninForm, LoginForm, CommentForm
from .addons import *

# Create your views here.

def index_view(request, tag='theme'):
	user = request.user
	if user.is_authenticated:
		data_user = get_object_or_404(DataUser, user=user)
	languages = Language.objects.all()
	return render(request, 'quizz/home.html', locals())

@login_required(login_url='login')
def choose_theme_view(request):
	user = request.user
	data_user = get_object_or_404(DataUser, user=user)
	req = request.POST
	if req:
		theme = get_object_or_404(Theme,id=req['theme_id'],language=data_user.language)
		if not theme.is_unlock(user):
			theme_required = ''
			for tag in theme.required.split():
				theme = get_object_or_404(Theme, tag=tag)
				theme_required += theme.name
			error = 'theme required '+theme_required
		elif theme.question_set.exists():
			request.session['error'] = False
			request.session['theme_id'] = req['theme_id']
			request.session['questions_id'] = [question.id for question in theme.question_set.all()]
			request.session['questions_id'] = mysort(request.session['questions_id'])
			return redirect('questions')
		else:
			error = "pas de question pour le moment"
	themes = []
	for theme in Theme.objects.filter(language=data_user.language):
		theme.unlock = theme.is_unlock(user)
		theme.is_completed = theme.tag in data_user.theme_valided.split()
		themes.append(theme)
	return render(request, 'quizz/choose_theme.html', locals())

@login_required(login_url='login')
def questions_view(request):
	user = request.user
	data_user = get_object_or_404(DataUser, user=user)
	can_comment = ''
	if not 'questions_id' in request.session:
		return redirect('choose_theme')
	elif not request.session['questions_id']:
		theme = Theme.objects.get(id=request.session['theme_id'])
		theme_full(data_user, theme, full=False)
		if not request.session['error']:
			theme_full(data_user, theme)
			bonus = 10
			data_user.score += bonus
		del request.session['theme_id']
		del request.session['questions_id']
		return render(request, 'quizz/finish.html', locals())
	else:
		questions_id = request.session['questions_id']
		question = Question.objects.get(id=questions_id[0])
		req = request.POST
		if req:
			choice = get_object_or_404(Choice, id=req['choice_id'])
			failure = True
			can_comment = True
			passed = True
			if question.answer_set.filter(answer_text=choice.choice_text).exists():
				questions_id = questions_id[1:]
				request.session['questions_id'] = questions_id
				failure = False
				data_user.score += 5
				data_user.save()
			else:
				#apres e choix du theme c'est true par default
				#s'il fait une erreur ca devient false et ca doit rester jusqu'a la garde
				request.session['error'] = True
		choices = question.choice_set.all()
		choices = mysort(choices)
		return render(request, 'quizz/questions.html', locals())

@login_required(login_url='login')
def comment_view(request, question_id):
	user = request.user
	req = request.POST
	if req:
		form = CommentForm(req)
		if form.is_valid():
			question = get_object_or_404(Question, id=question_id)
			comment_text = form.cleaned_data['comment_text']
			Comment.objects.create(question=question, user=user, comment_text=comment_text)
			return redirect('questions')
	form = CommentForm()
	question = get_object_or_404(Question ,id=question_id)
	return render(request, 'quizz/comment.html', locals())

@login_required(login_url='login')
def logout_view(request):
	lang = 'en' if not 'language' in request.session else request.session['language']
	logout(request)
	request.session['language'] = lang
	return redirect('home')

@login_required(login_url='login')
def account_view(request, user_id):
	user = get_object_or_404(User, id=user_id)
	data_user = get_object_or_404(DataUser, user=request.user)
	languages = Language.objects.all()
	return render(request, 'quizz/account.html', locals())

@login_required(login_url='login')
def ranking_view(request):
	data_user = get_object_or_404(DataUser, user=request.user)
	data_users = DataUser.objects.order_by('-score')
	return render(request, 'quizz/ranking.html', locals())

def signin_view(request):
	req = request.POST
	if req:
		form = SigninForm(req)
		if form.is_valid():
			language = get_object_or_404(Language, id=req['language_id'])
			user = form.save(commit=False)
			user.save()
			DataUser.objects.create(user=user, language=language)
			return redirect('login')
	else:
		form = SigninForm()
	return render(request, 'quizz/signin.html', {'form':form,'languages':Language.objects.all()})

def login_view(request):
	req = request.POST
	error = ''
	if req:
		form = LoginForm(req)
		if form.is_valid():
			#a revoir
			username_or_email = form.cleaned_data['username_or_email']
			password = form.cleaned_data['password']
			user = User.objects.filter(Q(username=username_or_email) | Q(email=username_or_email), password=password)
			if user:
				user = user[0]
				login(request, user)
				return redirect('home')
			else:
				error = "Nom d'utilisateur ou mot de passe invalide, reessayez encore"
	else:
		form = LoginForm()
	return render(request, 'quizz/login.html', {'error':error,'form':form})

def about_view(request):
	return render(request, 'quizz/about.html')

def setlanguage_view(request, code=None):
	if 'lang_id' in request.GET:
		lang_id = request.GET['lang_id']
		language = get_object_or_404(Language, id=lang_id)
		data_user = get_object_or_404(DataUser, user=request.user)
		data_user.language = language
		data_user.save()
	return redirect('home')