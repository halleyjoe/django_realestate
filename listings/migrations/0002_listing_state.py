# Generated by Django 3.1.7 on 2021-03-15 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='state',
            field=models.CharField(default=True, max_length=100),
            preserve_default=False,
        ),
    ]
