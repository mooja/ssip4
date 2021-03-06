# Generated by Django 2.0.4 on 2018-05-15 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='emergency_cellphone',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='emergency_comment',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='emergency_first_name',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='emergency_homephone',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='emergency_last_name',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='picture',
            field=models.ImageField(default=None, null=True, upload_to='members/'),
        ),
    ]
