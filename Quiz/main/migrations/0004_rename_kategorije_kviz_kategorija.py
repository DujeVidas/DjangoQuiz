# Generated by Django 4.1.2 on 2022-12-22 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_question_opispitanja_spajanjenapitanje'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kviz',
            old_name='kategorije',
            new_name='kategorija',
        ),
    ]
