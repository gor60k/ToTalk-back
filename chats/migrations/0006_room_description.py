# Generated by Django 5.0.3 on 2024-05-28 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0005_room_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
