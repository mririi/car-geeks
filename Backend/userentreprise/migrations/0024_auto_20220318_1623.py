# Generated by Django 3.0.3 on 2022-03-18 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userentreprise', '0023_auto_20220318_1519'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userentreprise',
            old_name='adresseE',
            new_name='addressE',
        ),
        migrations.AddField(
            model_name='userentreprise',
            name='country',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='userentreprise',
            name='nbEval',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=20),
        ),
    ]