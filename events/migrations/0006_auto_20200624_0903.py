# Generated by Django 3.0.7 on 2020-06-24 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20200624_0552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('cancel', 'Cancel'), ('running', 'Running'), ('finished', 'Finished')], max_length=10),
        ),
        migrations.AlterField(
            model_name='eventmember',
            name='attend_status',
            field=models.CharField(choices=[('attend', 'Attend'), ('absense', 'Absense')], max_length=10),
        ),
    ]
