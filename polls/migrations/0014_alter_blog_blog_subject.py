# Generated by Django 3.2.4 on 2021-06-27 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_alter_blog_blog_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_subject',
            field=models.CharField(max_length=1000),
        ),
    ]
