# Generated by Django 4.0.1 on 2022-03-31 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userprofile', '0012_alter_userprofile_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detailsP', models.CharField(blank=True, max_length=200, null=True)),
                ('accepted', models.BooleanField(default=False)),
                ('nblikes', models.IntegerField(default=0)),
                ('nbcomments', models.IntegerField(default=0)),
                ('datecreation', models.DateTimeField(auto_now_add=True)),
                ('imagePost', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('userprofilePost', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofile.userprofile')),
            ],
        ),
    ]