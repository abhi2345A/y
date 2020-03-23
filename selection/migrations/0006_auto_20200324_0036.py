# Generated by Django 3.0.2 on 2020-03-23 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0005_auto_20200323_0134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='father_name',
            new_name='journeyfrom',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='student_name',
            new_name='journeyto',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='room',
            new_name='seat',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='room_allotted',
            new_name='seat_allotted',
        ),
        migrations.AddField(
            model_name='student',
            name='passenger_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
