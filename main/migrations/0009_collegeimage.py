# Generated by Django 4.0.6 on 2022-10-01 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_events_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollegeImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('cover', models.ImageField(default='default.jpg', upload_to='covers')),
            ],
        ),
    ]
