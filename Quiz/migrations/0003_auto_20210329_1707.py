# Generated by Django 3.1.7 on 2021-03-29 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0002_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='quiz_id',
            new_name='quiz',
        ),
    ]
