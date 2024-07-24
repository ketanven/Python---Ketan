# Generated by Django 5.0.7 on 2024-07-23 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_institute', '0005_book_language_book_pages_book_published_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('mobile', models.BigIntegerField()),
                ('profile', models.ImageField(upload_to='picture/')),
                ('usertype', models.CharField(default='buyer', max_length=20)),
                ('institute', models.CharField(default='', max_length=100)),
            ],
        ),
    ]