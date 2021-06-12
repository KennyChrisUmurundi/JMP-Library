# Generated by Django 3.1.3 on 2021-06-01 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_auto_20210601_0923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrowed',
            name='borrower',
        ),
        migrations.AlterField(
            model_name='member',
            name='member_no',
            field=models.CharField(default='CF3A4', editable=False, max_length=50, unique=True),
        ),
    ]
