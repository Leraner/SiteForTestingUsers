# Generated by Django 4.0.5 on 2022-11-15 21:42

from django.db import migrations, models
import post.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(blank=True, default=post.models.set_random_default_cover, null=True, upload_to='post_cover/%Y/%m/%d/'),
        ),
    ]
