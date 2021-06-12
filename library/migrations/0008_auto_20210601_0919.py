# Generated by Django 3.1.3 on 2021-06-01 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_auto_20210601_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowed',
            name='member_no',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='member_no',
            field=models.CharField(default='A65FC', editable=False, max_length=50, unique=True),
        ),
    ]
