# Generated by Django 4.1.7 on 2023-02-21 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_a7aniiik_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='a7aniiik',
            name='joined_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='a7aniiik',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]