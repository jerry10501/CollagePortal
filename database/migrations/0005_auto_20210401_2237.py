# Generated by Django 3.1.7 on 2021-04-01 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_auto_20210401_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
