# Generated by Django 4.1.4 on 2022-12-12 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='desctiption',
            new_name='description',
        ),
    ]
