# Generated by Django 5.0.3 on 2024-05-28 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0007_category_avatar_room_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='chats/rooms/'),
        ),
    ]
