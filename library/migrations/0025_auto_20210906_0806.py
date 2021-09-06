# Generated by Django 3.2.4 on 2021-09-06 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0024_auto_20210825_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_no',
            field=models.CharField(default='590A', editable=False, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_no',
            field=models.CharField(default='B1675', editable=False, max_length=50, unique=True),
        ),
    ]
