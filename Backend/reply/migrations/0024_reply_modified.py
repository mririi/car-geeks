# Generated by Django 4.0.1 on 2022-03-19 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reply', '0023_alter_reply_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='modified',
            field=models.BooleanField(default=False),
        ),
    ]