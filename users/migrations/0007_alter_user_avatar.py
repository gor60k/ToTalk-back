# Generated by Django 5.0.3 on 2024-05-28 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='/users/avatars/default.jpg', upload_to='users/avatars/'),
        ),
    ]
