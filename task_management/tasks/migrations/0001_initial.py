# Generated by Django 4.2.8 on 2023-12-20 09:16

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
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('status', models.BooleanField(choices=[(False, 'Incomplete'), (True, 'Complete')], default=False)),
                ('priority', models.IntegerField(choices=[(0, 'Low'), (1, 'Medium'), (2, 'High')], default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
