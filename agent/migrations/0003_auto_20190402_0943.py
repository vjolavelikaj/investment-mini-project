# Generated by Django 2.2 on 2019-04-02 09:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('agent', '0002_auto_20190402_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investor',
            name='type',
            field=models.IntegerField(choices=[(1, 'Person'), (2, 'Institution')]),
        ),
    ]
