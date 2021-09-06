# Generated by Django 3.2.4 on 2021-07-31 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0013_auto_20210731_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='plan',
            field=models.CharField(default='basic', max_length=200),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_no',
            field=models.CharField(default='A51F', editable=False, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_no',
            field=models.CharField(default='A9174', editable=False, max_length=50, unique=True),
        ),
    ]
