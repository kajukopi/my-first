# Generated by Django 3.2.4 on 2021-06-27 15:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.RenameField(
            model_name='choice',
            old_name='question',
            new_name='pertanyaan',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='choice_text',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='votes',
        ),
        migrations.AddField(
            model_name='choice',
            name='subject',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
    ]
