# Generated by Django 3.0.3 on 2022-04-01 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0012_evaluation_commenteval'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]