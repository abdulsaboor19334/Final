# Generated by Django 3.1 on 2020-09-05 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0004_auto_20200905_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
