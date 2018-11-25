from django.urls import path
from . import views

urlpatterns = [
	path('', views.index_view, name='home'),
	path('signin/', views.signin_view, name='signin'),
	path('login/', views.login_view, name='login'),
	path('logout/', views.logout_view, name='logout'),
	path('choose_theme/', views.choose_theme_view, name='choose_theme'),
	path('questions/', views.questions_view, name='questions'),
	path('comment/<int:question_id>/', views.comment_view, name='comment'),
	path('account/<int:user_id>/', views.account_view, name='account'),
	path('ranking/', views.ranking_view, name='ranking'),
	path('about/', views.about_view, name='about'),
	path('setlanguage/', views.setlanguage_view, name='setlanguage'),
	path('setlanguage/<str:code>/', views.setlanguage_view, name='setlanguage')
]
