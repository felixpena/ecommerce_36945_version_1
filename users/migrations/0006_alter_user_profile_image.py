# Generated by Django 4.0.4 on 2022-06-18 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='image',
            field=models.ImageField(default='', upload_to='profile_image'),
        ),
    ]
