# Generated by Django 4.0.1 on 2022-03-24 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicetype', '0003_auto_20220323_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicetype',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]