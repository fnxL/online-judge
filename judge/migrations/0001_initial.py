# Generated by Django 3.1.7 on 2021-03-31 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problemid', models.IntegerField()),
                ('status', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'Data',
            },
        ),
        migrations.CreateModel(
            name='Problems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('problem_statement', models.TextField()),
                ('input_data', models.TextField()),
                ('output_data', models.TextField()),
                ('test_cases', models.TextField()),
                ('correct_output', models.TextField()),
                ('difficulty', models.IntegerField()),
                ('time_limit', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Problems',
            },
        ),
        migrations.CreateModel(
            name='Submissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problemid', models.IntegerField()),
                ('sourcecode', models.TextField()),
                ('verdict', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Submissions',
            },
        ),
    ]