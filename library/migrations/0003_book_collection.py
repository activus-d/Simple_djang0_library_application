# Generated by Django 4.1.7 on 2023-03-16 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_collection_alter_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='collection',
            field=models.ManyToManyField(to='library.collection'),
        ),
    ]
