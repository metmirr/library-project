# Generated by Django 3.0rc1 on 2019-12-28 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publication_date',
            field=models.DateField(auto_now=True),
        ),
    ]