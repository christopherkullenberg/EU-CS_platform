# Generated by Django 2.2.10 on 2020-06-04 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0042_auto_20200604_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='keywords',
            field=models.ManyToManyField(blank=True, to='projects.Keyword'),
        ),
    ]
