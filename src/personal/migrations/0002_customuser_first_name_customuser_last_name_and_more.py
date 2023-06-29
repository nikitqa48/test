# Generated by Django 4.2.2 on 2023-06-29 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=500, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=500, null=True, verbose_name='Фамилия'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='middle_name',
            field=models.CharField(max_length=500, null=True, verbose_name='Отчество'),
        ),
    ]
