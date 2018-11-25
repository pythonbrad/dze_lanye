#Developper avec Django2.x

#started 02/08/2018 20:06

#quizV0.x 02/08/2018 20:06
*Cette version n'etait que console*
- Creation de la base de donnee
- Creation d'un fichier tests.py

#quizV1.x 08/08/2018 20:11
- Creation d'une interface web
- Possibiliter de s'inscrire
- Possibiliter de choisir theme
- Possibiliter de choisir plusieurs reponses
- Possibiter de voir son score
- Posibiliter de commenter une reponse

#quizV1.x 10/08/2018 20:48
- Utilisation de django.forms
- Creation des formulaires suivants SigninForm, LoginForm, CommentForm
- La date de naissance lors de l'inscription n'est plus demandee
- Amelioration de la gestion d'erreur
- Les themes passer sont marquees (2 fois orange, 4 fois rouge)
- Possibiliter de voir ses infos d'evolution
- Suppression du fichier tests.py (il n'etais plus adapter a la version et c'est un peu penible de le maintenir)

#quizzV1.x 11/08/2018 18:54
- Suppression du model Account
- Utilisation de django.contrib.auth
- Creation d'un models DataUser avec pour ForeignKey User
- Les themes passer sont marquees en vert
- Possibiliter de voir son classement
- Possibiliter de consulter le compte d'autre personne
- Creation d'un ValidationError dans le formulaire SigninForm

#quizV1.x 13/08/2018 08:50
- Creation d'un fichier addons.py
- Creation d'une fonction mysort
- Creation du model Language
- Remplacement de la relation ManyToManyField Theme par ForeignKey Theme dans le model Question
- Insertion des ForeignKey Language dans les models DataUser et Theme
- Modification du fichier admin.py
- Creation de la vue about_view

#quizV1.x 15/08/2018 00:00
- Creation d'un systeme de traduction
- Creation d'un module mytranslate
- Creation d'un chargeur de donnee de langue
- Creation de la fonction mytrans dans le fichier addons.py
- Ajout du francais
- Ajout de l'anglais
- Utilisation django.middleware.locale.LocaleMiddleware

#quizV1.x 15/08/2018 13:30
- Ajout d'une variable safe dans addons.mytrans de addons.py
- Possibiliter de passer comme argument la langue principale dans addons.mytrans
- Ajout de la fonction addons.getlistlang
- Utilisation de django.utils.translation.activate
- Ajout de la vue setlanguage_view
- Ajout du tag getlistlang dans mytrans.py
- Correction du probleme de case des donnes de traduction dans build_mylang.py
- Ajout d'un systeme de changement de langue instantanement

#quizV1.x 15/08/2018 16:23
- Correction d'un bug au niveau des themes requis

#quizV1.x 16/08/2018 12:01
- Modification dans addons.mytrans "safe = settings.DEBUG"
- Modification dans settings.ALLOWED_HOSTS
- Utilisation de addons.mysort au niveau de la creation de la session questions_id in la vue choose_theme_view
- Utilisation de addons.mytrans pour la traduction des ValidationError
- Configuration de addons.mytrans "mainlang=settings.LANGUAGE_CODE"
- Changement au niveau de settings.py 'LANGUAGE_CODE="fr-FR"'
- Bug et probleme de traduction au niveau des templates
- Correction des problemes d'accents
- Ajout d'une condition "if safe" dans addons.mytrans

#quizV1.x 18/08/2018 18:52
- Modification de admin.py
- Correction d'un probleme de conservation de la language apres deconnexion
- Creation d'une page d'acceuil
- Remplacement de "nombre de fois un theme a ete passee" pr "nombre de theme passee"
- Possibiliter de changer de language a tout moment
- Changement du classement en classement general

#consulter bitbucket