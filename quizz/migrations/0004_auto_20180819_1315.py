# Generated by Django 2.1 on 2018-08-19 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0003_auto_20180813_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='tag',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]