# Generated by Django 3.2.4 on 2021-06-27 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20210627_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pertanyaan',
            name='pub_tgl',
            field=models.DateTimeField(verbose_name='tanggal dipublis'),
        ),
    ]
