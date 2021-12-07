# Generated by Django 3.2 on 2021-04-20 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20210419_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='phone',
            field=models.CharField(default=1, max_length=13, verbose_name='Номер телефона'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='instructor',
            name='login',
            field=models.EmailField(max_length=50, verbose_name='Логин'),
        ),
        migrations.AlterField(
            model_name='student',
            name='login',
            field=models.EmailField(max_length=50, verbose_name='Логин'),
        ),
    ]