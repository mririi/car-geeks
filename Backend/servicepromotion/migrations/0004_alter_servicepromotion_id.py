# Generated by Django 4.0.1 on 2022-03-18 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicepromotion', '0003_auto_20220318_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicepromotion',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]