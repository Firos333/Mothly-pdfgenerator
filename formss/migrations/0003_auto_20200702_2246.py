# Generated by Django 3.0.4 on 2020-07-02 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formss', '0002_auto_20200702_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
