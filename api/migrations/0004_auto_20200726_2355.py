# Generated by Django 3.0.7 on 2020-07-26 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200726_1955'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['created_on']},
        ),
    ]
