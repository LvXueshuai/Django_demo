# Generated by Django 2.1 on 2018-08-29 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lxs', '0003_auto_20180829_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
