# Generated by Django 2.1.1 on 2018-12-02 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_favorites_fooditem_rates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='establishment',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]