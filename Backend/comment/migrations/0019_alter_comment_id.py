# Generated by Django 4.0.1 on 2022-03-16 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0018_auto_20220315_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]