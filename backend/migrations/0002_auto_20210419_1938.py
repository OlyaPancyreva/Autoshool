# Generated by Django 3.2 on 2021-04-19 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Наименование')),
                ('date_start', models.DateField(verbose_name='Начало обучения')),
                ('date_end', models.DateField(verbose_name='Окончание обучения')),
                ('date_exam', models.DateField(verbose_name='Дата сдачи экзаменов')),
                ('category', models.CharField(max_length=3, verbose_name='Категория обучения')),
                ('teacher', models.CharField(max_length=100, verbose_name='Преподаватель')),
            ],
            options={
                'verbose_name': 'Группа обучения',
                'verbose_name_plural': 'Группы обучения',
            },
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=100, verbose_name='ФИО инструктора')),
                ('car', models.CharField(max_length=100, verbose_name='Машина')),
                ('login', models.CharField(max_length=50, verbose_name='Логин')),
                ('password', models.CharField(max_length=50, verbose_name='Пароль')),
            ],
            options={
                'verbose_name': 'Инструктор',
                'verbose_name_plural': 'Инструкторы',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(verbose_name='Дата и время занятия')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.instructor', verbose_name='Инструктор')),
            ],
            options={
                'verbose_name': 'Расписание вождения',
                'verbose_name_plural': 'Расписания вождения',
            },
        ),
        migrations.AlterModelOptions(
            name='request',
            options={'verbose_name': 'Заявка на обучение', 'verbose_name_plural': 'Заявки на обучение'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Статус', 'verbose_name_plural': 'Статусы'},
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=100, verbose_name='ФИО ученика')),
                ('birthday', models.DateField(verbose_name='Дата рождения')),
                ('drive_count', models.PositiveSmallIntegerField(default=16, verbose_name='Кол-во часов вождения')),
                ('login', models.CharField(max_length=50, verbose_name='Логин')),
                ('password', models.CharField(max_length=50, verbose_name='Пароль')),
                ('drive', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.schedule', verbose_name='Следующее занятие по вождению')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.group', verbose_name='Группа')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.instructor', verbose_name='Инструктор')),
            ],
        ),
    ]
