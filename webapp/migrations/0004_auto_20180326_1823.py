# Generated by Django 2.0.2 on 2018-03-26 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20180305_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumin',
            name='sl_no',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='issuein',
            name='sl_no',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
