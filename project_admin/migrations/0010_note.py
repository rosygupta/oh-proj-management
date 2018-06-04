# Generated by Django 2.0.5 on 2018-06-04 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_admin', '0009_auto_20180523_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_admin.ProjectMember')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_admin.Project')),
            ],
        ),
    ]
