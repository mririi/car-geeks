# Generated by Django 3.0.3 on 2022-03-03 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartype', '0004_alter_cartype_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartype',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]