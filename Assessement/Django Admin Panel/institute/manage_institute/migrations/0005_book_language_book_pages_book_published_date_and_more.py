# Generated by Django 5.0.7 on 2024-07-20 15:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_institute', '0004_club_founded_date_club_members_count_club_president_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.CharField(choices=[('English', 'English'), ('Spanish', 'Spanish'), ('French', 'French')], default='English', max_length=20),
        ),
        migrations.AddField(
            model_name='book',
            name='pages',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='published_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(default='Unknown Author', max_length=200),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(default='0000000000000', max_length=13, unique=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(default='Untitled', max_length=200),
        ),
    ]