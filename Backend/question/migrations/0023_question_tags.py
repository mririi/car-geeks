# Generated by Django 3.0.3 on 2022-03-18 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0022_auto_20220318_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]