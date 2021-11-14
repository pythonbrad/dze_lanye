# Le debut
J'etais entrain de lire un tuto sur Django que mon frere m'avait recommander et j'ai commencer a trouver django agreable. Le cour etait diviser en deux parties, la base de django et la parti avancee. Quand j'ai fini de lire la base, on m'a demande de realiser un projet de petit blog et d'envoyer. J'ai realiser et envoyer, le project. J'ai meme eu 9/10. Je n'etais plus motiver a continuer le tuto, j'ai donc decider de realiser un autre projet pour plus apprendre Django.

# Pourquoi un quizz sur les langues maternelles
En fouillant mon onedrive, je suis tomber sur mon vieux projet de learn_bamileke. J'ai decider de le refaire en l'ameliorant mais, a un niveau j'ai trouver que c'etais mieux de stocker les donnees en ligne et de faire un web service. Je voulait faire comme l'app Duolingo, c'est alors la que j'ai creer la version 0.x de mon quizz. J'ai d'abord creer un script python pour le tester et ca fonctionnait bien. Je suis passer a la version 1.0 et j'ai arreter de maintenir le script python. Et c'est comme ca que j'ai continuer a ameliorer le quizz.

# Comment l'utiliser (coter client)
- Tout d'abord il faut s'inscrire, remplir le formulaire et n'oublier surtout pas de choisir la langue
- Ensuite il faut se connecter et le tour est jouer
- Vous pouvez voir votre classement si ca vous interresse.

# Comment l'utiliser (coter administrateur ou personnel)
*Je recommande l'utilisation de Django 2.x, les versions anterieurs ne permmettent pas a un personnel d'avoir uniquement le droit de spectateur*
*Je ferais peut etre un tuto dessus*
- Vous pouvez creer des utilisateurs qui auront acces a des droits precis, comme gerer les langues, gerer les questions, gerer les reponses, gerer les logs, etc... Et pouvez aussi modifier le 'gerer' en ajouter, modifier, supprimer.
- NB: Un administrateur ou personnel ne peut pas etre un utilisateur du site, mais l'inverse est possible (je ne le recommande pas, mais dans ce cas, pour jouir de ses droits, il devra se connecter a travers le site et non a travers le panel d'administration)>

# Comment l'utiliser au niveau du code
*Je creerais un fichier tests.py*

# Deployement
Peut prendre 10min avec sqlite3
# copy and past it
```shell
git clone https://github.com/pythonbrad/dze_lanye.git
cd dze_lanye
pip install virtualenv
mkvirtualenv myvirtualenv --python=/usr/bin/python3.6
workon myvirtualenv
pip install django==2.1
pip install mysqlclient
pip install pillow
git clone http://github.com/pythonbrad/brad_blog.git
git clone http://github.com/pythonbrad/data_lang.git
git clone http://github.com/pythonbrad/conj_nufi.git
python manage.py makemigrations
python manage.py migrate
python manage.py shell
```

```python
from insert_in_database_django_datalang import *
run(Language ,Theme, Question, Answer, Choice)
all
exit()
```

```shell
manage.py runserver
```
And wait, ca peut prende du temps avec sqlite3


# Screenshot

![Image](https://github.com/pythonbrad/dze_lanye/blob/master/screen.png)
