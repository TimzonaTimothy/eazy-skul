# Generated by Django 4.1.5 on 2023-02-03 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clearance_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('reg_no', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=300)),
                ('phone', models.BigIntegerField()),
                ('department', models.CharField(max_length=200)),
                ('level', models.CharField(max_length=100)),
                ('school', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='clearances_expalain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('body', models.CharField(blank=True, max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='contact_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(blank=True, max_length=300)),
                ('address2', models.CharField(blank=True, max_length=300)),
                ('tel1', models.CharField(blank=True, max_length=50)),
                ('tel2', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='contactz_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.BigIntegerField()),
                ('subject', models.CharField(max_length=300)),
                ('suggestion', models.CharField(max_length=5000)),
                ('message', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='exam_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('reg_no', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.BigIntegerField()),
                ('department', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=7000)),
                ('school', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='howtoz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('body', models.CharField(blank=True, max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='pd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300)),
                ('body', models.CharField(blank=True, max_length=4000)),
            ],
        ),
        migrations.CreateModel(
            name='project_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('regno', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=300)),
                ('department', models.CharField(max_length=300)),
                ('phone', models.BigIntegerField()),
                ('message', models.CharField(max_length=2000)),
                ('project_topic', models.CharField(max_length=2000)),
                ('school', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='registration_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('app_no', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=300)),
                ('phone', models.BigIntegerField()),
                ('department', models.CharField(max_length=300)),
                ('level', models.CharField(max_length=30)),
                ('school', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='regular_assessment_tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('reg_no', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.BigIntegerField()),
                ('department', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=5000)),
                ('school', models.CharField(blank=True, max_length=500)),
            ],
        ),
    ]
