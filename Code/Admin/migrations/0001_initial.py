# Generated by Django 2.0.3 on 2018-04-14 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Year', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=100)),
                ('class_teacher', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Year', models.CharField(max_length=100)),
                ('Rank', models.IntegerField()),
                ('cl_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.Class')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('p_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=1000)),
                ('cl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.Class')),
            ],
        ),
        migrations.CreateModel(
            name='TotalMarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('T_Year', models.CharField(max_length=100)),
                ('T_cl_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.Class')),
            ],
        ),
        migrations.AddField(
            model_name='results',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.Student'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.Student'),
        ),
    ]
