# Generated by Django 3.0.7 on 2020-12-06 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('password_history', '0002_auto_20180424_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpasswordhistoryconfig',
            name='iterations',
            field=models.IntegerField(blank=True, default=None, editable=False, null=True, verbose_name='The number of iterations for hasher'),
        ),
    ]
