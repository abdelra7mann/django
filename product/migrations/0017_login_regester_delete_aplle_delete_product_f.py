# Generated by Django 4.1.7 on 2023-02-26 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_pssword_data_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=150)),
                ('Password', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Regester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(blank=True, max_length=55, null=True)),
                ('lastName', models.CharField(blank=True, max_length=55, null=True)),
                ('Email', models.CharField(blank=True, max_length=55, null=True)),
                ('password', models.CharField(blank=True, max_length=55, null=True)),
                ('userName', models.CharField(blank=True, max_length=55, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Aplle',
        ),
        migrations.DeleteModel(
            name='Product_F',
        ),
    ]
