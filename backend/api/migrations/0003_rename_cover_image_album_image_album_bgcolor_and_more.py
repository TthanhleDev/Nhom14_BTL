# Generated by Django 5.1.7 on 2025-03-25 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_artist_album_song_playlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='cover_image',
            new_name='image',
        ),
        migrations.AddField(
            model_name='album',
            name='bgColor',
            field=models.CharField(default='#2a4365', max_length=100),
        ),
        migrations.AddField(
            model_name='album',
            name='desc',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='song',
            name='desc',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='song',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='album_covers/'),
        ),
    ]
