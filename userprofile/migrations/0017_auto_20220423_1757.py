# Generated by Django 3.0.3 on 2022-04-23 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0016_auto_20220423_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='tel',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=20),
        ),
    ]