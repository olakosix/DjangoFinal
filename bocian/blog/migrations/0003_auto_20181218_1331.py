# Generated by Django 2.1.4 on 2018-12-18 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20181218_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wpis',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='wpis',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
