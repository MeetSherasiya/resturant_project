# Generated by Django 4.1.6 on 2023-04-02 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resturantapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_time',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='book',
            name='people',
            field=models.CharField(max_length=3),
        ),
    ]
