# Generated by Django 4.1.2 on 2022-12-22 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_kategorije_kviz_kategorija'),
    ]

    operations = [
        migrations.AddField(
            model_name='pitanje',
            name='naziv',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
