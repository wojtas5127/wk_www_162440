# Generated by Django 4.2.9 on 2024-01-03 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='shirt_size',
            field=models.CharField(choices=[('M', 'Male'), ('S', 'Srednie'), ('D', 'duze')], default='M', max_length=1),
        ),
    ]
