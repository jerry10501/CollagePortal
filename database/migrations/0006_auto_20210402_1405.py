# Generated by Django 3.1.7 on 2021-04-02 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_auto_20210401_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='FILE',
            field=models.FileField(blank=True, default='', upload_to='Assignments/'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='FILE',
            field=models.FileField(blank=True, default='', upload_to='Submissions/'),
        ),
    ]
