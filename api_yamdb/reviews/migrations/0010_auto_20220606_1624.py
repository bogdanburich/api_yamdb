# Generated by Django 2.2.16 on 2022-06-06 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0009_auto_20220603_1842'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='review',
            name='unique_title_author',
        ),
    ]
