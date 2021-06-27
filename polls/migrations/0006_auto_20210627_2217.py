# Generated by Django 3.2.4 on 2021-06-27 15:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20210627_2216'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='pertanyaan',
            new_name='question',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='subject',
        ),
        migrations.AddField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='choice',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Isi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=1000)),
                ('pertanyaan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.question')),
            ],
        ),
    ]
