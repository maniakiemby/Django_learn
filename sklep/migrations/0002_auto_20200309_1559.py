# Generated by Django 3.0.4 on 2020-03-09 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sklep', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='descriptions',
            new_name='description',
        ),
    ]
