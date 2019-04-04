# Generated by Django 2.2 on 2019-04-02 09:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('investment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='status',
            field=models.IntegerField(choices=[(1, 'New'), (2, 'In progress'), (3, 'Finished')], max_length=20,
                                      null=True),
        ),
    ]