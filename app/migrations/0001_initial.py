# Generated by Django 5.0.3 on 2024-04-05 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskTitle', models.CharField(max_length=30)),
                ('taskDesc', models.TextField(max_length=300)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
