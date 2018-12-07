from django.contrib import admin
from .models import Question, Choice, Theme, Remark, DataUser, Answer, Language

class ChoiceInline(admin.StackedInline):
	model = Choice
	extra = 1

class AnswerInline(admin.StackedInline):
	model = Answer
	extra = 1

class AnswerAdmin(admin.ModelAdmin):
	list_display = ['answer_text', 'question', 'get_language', 'get_theme']
	search_fields = ['answer_text', 'question__question_text']

	def get_language(self, obj):
		return obj.question.theme.language
	get_language.short_description = 'Language'

	def get_theme(self, obj):
		return obj.question.theme
	get_theme.short_description = 'Theme'

class QuestionAdmin(admin.ModelAdmin):
	list_display = ['question_text', 'theme']
	fields = ['question_text', 'theme']
	inlines = [AnswerInline, ChoiceInline]
	list_filter = ['theme']
	search_fields = ['question_text', 'theme__name']

class ThemeAdmin(admin.ModelAdmin):
	list_display = ['name', 'level', 'tag', 'required', 'language']
	list_filter = ['language']
	search_fields = ['name']

class RemarkAdmin(admin.ModelAdmin):
	list_display = ['user', 'question', 'remark_text', 'pub_date', 'is_recent', 'is_visible', 'get_language']
	list_filter = ['pub_date']
	exclude = ['pub_date']
	search_fields = ['remark_text', 'question__question_text']

	def get_language(self, obj):
		return obj.question.theme.language
	get_language.short_description = 'Language'

class DataUserAdmin(admin.ModelAdmin):
	list_display = ['user', 'score', 'how_many_theme_valided', 'how_many_theme_passed', 'language']
	list_filter = ['language']

	def how_many_theme_valided(self, obj):
		return len(obj.theme_valided.split())

	def how_many_theme_passed(self, obj):
		return len(obj.theme_passed.split())


# Register your models here.
admin.site.register(Theme, ThemeAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Remark, RemarkAdmin)
admin.site.register(DataUser, DataUserAdmin)
admin.site.register(Language)