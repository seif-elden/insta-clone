# Generated by Django 3.1.5 on 2021-01-29 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='more_user_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('phone_number', models.CharField(blank=True, max_length=50, null=True)),
                ('bio', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_info', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('caption', models.CharField(blank=True, max_length=50)),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User_uploaded_files', to=settings.AUTH_USER_MODEL)),
                ('post_more_user_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='more_user_info', to='account.more_user_info')),
            ],
        ),
        migrations.CreateModel(
            name='follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followed_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='followed_user', to=settings.AUTH_USER_MODEL)),
                ('followers', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='followers', to=settings.AUTH_USER_MODEL)),
                ('more_followed_user_info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='more_followed_user_info', to='account.more_user_info')),
                ('more_follower_info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='more_follower_info', to='account.more_user_info')),
            ],
        ),
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=100)),
                ('created_dt', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('created_by_photo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photo_of_comment', to='account.more_user_info')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='account.photo')),
            ],
        ),
    ]
